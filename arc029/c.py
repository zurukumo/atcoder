import sys

input = sys.stdin.readline

N, M = map(int, input().split())
c = [int(input()) for _ in range(N)]
abr = [[int(i) for i in input().split()] for _ in range(M)]

sch = []
for i in range(N):
    sch.append((c[i], 0, i + 1))
for a, b, r in abr:
    sch.append((r, a, b))
sch.sort()


class UnionFind:
    def __init__(self, N):
        self.parent = [-1] * N

    def root(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            if self.parent[rx] > self.parent[ry]:
                self.parent[rx] = ry
            else:
                if self.parent[rx] == self.parent[ry]:
                    self.parent[rx] -= 1
                self.parent[ry] = rx

    def same(self, x, y):
        return self.root(x) == self.root(y)


UF = UnionFind(N + 1)

ret = 0
for cost, x, y in sch:
    if not UF.same(x, y):
        UF.unite(x, y)
        ret += cost

print(ret)
