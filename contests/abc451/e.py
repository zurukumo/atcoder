import sys

input = sys.stdin.readline

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N - 1)]


class UnionFind:
    def __init__(self, N):
        self.parents = [-1] * N
        self.units = N

    def root(self, x):
        while self.parents[x] >= 0:
            x = self.parents[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            self.units -= 1
            if self.parents[rx] > self.parents[ry]:
                self.parents[rx] = ry
            else:
                if self.parents[rx] == self.parents[ry]:
                    self.parents[rx] -= 1
                self.parents[ry] = rx

    def same(self, x, y):
        return self.root(x) == self.root(y)


edges = [[] for _ in range(10000)]
for u in range(N):
    for v in range(u + 1, N):
        edges[A[u][v - u - 1]].append((u, v))

uf = UnionFind(N)
vec = [[] for _ in range(N)]
for cost in range(10000):
    for u, v in edges[cost]:
        if not uf.same(u, v):
            vec[u].append((v, cost))
            vec[v].append((u, cost))
            uf.unite(u, v)


dist = [0] * N
for i in range(N - 1):
    queue = [(i, -1)]
    dist[i] = 0

    while queue:
        cur, pre = queue.pop()
        for nex, cost in vec[cur]:
            if nex != pre:
                dist[nex] = dist[cur] + cost
                queue.append((nex, cur))

    if dist[i + 1 :] != A[i]:
        print("No")
        exit()


print("Yes")
