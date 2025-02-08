import sys

sys.setrecursionlimit(10**6)

N = int(input())
A = [int(i) for i in input().split()]


class StronglyConnectedComponent:
    def __init__(self, n):
        self.n = n
        self.G = [[] for _ in range(n)]
        self.rG = [[] for _ in range(n)]
        self.vs = []
        self.used = [False] * n
        self.cmp = [0] * n

    def add_edge(self, fr, to):
        self.G[fr].append(to)
        self.rG[to].append(fr)

    def dfs(self, v):
        self.used[v] = True
        for i in range(len(self.G[v])):
            if not self.used[self.G[v][i]]:
                self.dfs(self.G[v][i])
        self.vs.append(v)

    def rdfs(self, v, k):
        self.used[v] = True
        self.cmp[v] = k
        for i in range(len(self.rG[v])):
            if not self.used[self.rG[v][i]]:
                self.rdfs(self.rG[v][i], k)

    def scc(self):
        self.used = [False] * self.n
        for i in range(self.n):
            if not self.used[i]:
                self.dfs(i)
        self.used = [False] * self.n
        k = 0
        for i in reversed(self.vs):
            if not self.used[i]:
                self.rdfs(i, k)
                k += 1

        groups = [[] for _ in range(k)]
        for i in range(self.n):
            groups[self.cmp[i]].append(i)

        return groups


ret = 0

scc = StronglyConnectedComponent(N)
for i, a in enumerate(A):
    scc.add_edge(i, a - 1)
    if i == a - 1:
        ret += 1

for group in scc.scc():
    if len(group) > 1:
        ret += len(group)


print(ret)
