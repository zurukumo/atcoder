import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
ABC = [[int(i) for i in input().split()] for _ in range(M)]

edges = []
for a, b, c in ABC:
    a -= 1
    b -= 1
    heapq.heappush(edges, (c, a, b))


class UnionFind:
    def __init__(self, N):
        self.parents = [-1] * N
        self.sizes = [1] * N
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
                self.sizes[ry] += self.sizes[rx]
            else:
                if self.parents[rx] == self.parents[ry]:
                    self.parents[rx] -= 1
                self.parents[ry] = rx
                self.sizes[rx] += self.sizes[ry]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def height(self, x):
        return -self.parents[self.root(x)]

    def size(self, x):
        return self.sizes[self.root(x)]


uf = UnionFind(N)
ret = 0
while edges:
    c, a, b = heapq.heappop(edges)
    if not uf.same(a, b) or c <= 0:
        uf.unite(a, b)
    else:
        ret += c

print(ret)
