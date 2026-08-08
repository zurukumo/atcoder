import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


# Kosaraju's algorithm
class StronglyConnectedComponent:
    def __init__(self, n):
        self.n = n
        self.G = [[] for _ in range(n)]
        self.rG = [[] for _ in range(n)]
        self.vs = []
        self.cmp = [0] * n

    def add_edge(self, fr, to):
        self.G[fr].append(to)
        self.rG[to].append(fr)

    def __dfs(self, v):
        # 2026-08-06: Pythonは再帰が遅いので再帰を使わずキューで
        # self.used[v] = True
        # for i in range(len(self.G[v])):
        #     if not self.used[self.G[v][i]]:
        #         self.__dfs(self.G[v][i])
        # self.vs.append(v)
        stack = [(v, 0)]
        while stack:
            node, state = stack.pop()
            if state == 0:
                if self.used[node]:
                    continue
                self.used[node] = True
                stack.append((node, 1))
                for to in reversed(self.G[node]):
                    if not self.used[to]:
                        stack.append((to, 0))
            else:
                self.vs.append(node)

    def __rdfs(self, v, k):
        # 2026-08-06: Pythonは再帰が遅いので再帰を使わずキューで
        # self.used[v] = True
        # self.cmp[v] = k
        # for i in range(len(self.rG[v])):
        #     if not self.used[self.rG[v][i]]:
        #         self.__rdfs(self.rG[v][i], k)
        stack = [v]
        self.used[v] = True
        while stack:
            node = stack.pop()
            self.cmp[node] = k
            for to in self.rG[node]:
                if not self.used[to]:
                    self.used[to] = True
                    stack.append(to)

    def scc(self):
        self.used = [False] * self.n
        for i in range(self.n):
            if not self.used[i]:
                self.__dfs(i)
        self.used = [False] * self.n
        k = 0
        for i in reversed(self.vs):
            if not self.used[i]:
                self.__rdfs(i, k)
                k += 1

        groups = [[] for _ in range(k)]
        for i in range(self.n):
            groups[self.cmp[i]].append(i)

        return groups


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    W = int(input())
    S = [input() for _ in range(N)]

    scc = StronglyConnectedComponent(N * W)
    for u, v in UV:
        u -= 1
        v -= 1
        for d in range(W):
            if S[u][d] == "o" and S[v][(d + 1) % W] == "o":
                scc.add_edge(u * W + d, v * W + (d + 1) % W)
            if S[v][d] == "o" and S[u][(d + 1) % W] == "o":
                scc.add_edge(v * W + d, u * W + (d + 1) % W)
    for u in range(N):
        for d in range(W):
            if S[u][d] == "o" and S[u][(d + 1) % W] == "o":
                scc.add_edge(u * W + d, u * W + (d + 1) % W)

    for group in scc.scc():
        if len(group) > 1 and any(e % W == 0 for e in group):
            print("Yes")
            break
    else:
        print("No")
