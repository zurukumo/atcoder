import sys

sys.setrecursionlimit(10**7)

N = int(input())
uv = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
xy = [[int(i) for i in input().split()] for _ in range(Q)]


class CycleFinder:
    def __init__(self, n, graph):
        self.n = n
        self.graph = graph
        self.seen = [False] * n
        self.finished = [False] * n
        self.group = 0
        self.groups = [-1] * n
        self.history = []

    def __dfs(self, pre, cur, is_prohibited_reverse=True):
        self.seen[cur] = True
        self.groups[cur] = self.group
        self.history.append(cur)

        for nex in self.graph[cur]:
            if is_prohibited_reverse and pre == nex:
                continue

            if self.finished[nex]:
                continue

            if self.groups[nex] != -1 and self.groups[nex] != self.group:
                continue

            if self.seen[nex] and not self.finished[nex]:
                return nex

            pos = self.__dfs(cur, nex, is_prohibited_reverse)
            if pos != -1:
                return pos

        self.finished[cur] = True
        self.history.pop()
        return -1

    def __reconstruct(self, pos):
        cycle = []
        while self.history:
            cur = self.history.pop()
            cycle.append(cur)
            if cur == pos:
                break

        return cycle

    def detect(self, is_prohibited_reverse=True):
        cycles = []
        for cur in range(self.n):
            if self.seen[cur]:
                continue
            self.history = []
            pos = self.__dfs(-1, cur, is_prohibited_reverse)
            if pos != -1:
                cycles.append(self.__reconstruct(pos))
            self.group += 1
        return cycles


graph = [[] for _ in range(N)]
for u, v in uv:
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

cf = CycleFinder(N, graph)
loop = set(cf.detect()[0])

parent = [-1] * N
for start in loop:
    stack = [start]
    while stack:
        cur = stack.pop()
        parent[cur] = start
        for nex in graph[cur]:
            if parent[nex] == -1 and nex not in loop:
                stack.append(nex)


for x, y in xy:
    x -= 1
    y -= 1
    if parent[x] == parent[y]:
        print("Yes")
    else:
        print("No")
