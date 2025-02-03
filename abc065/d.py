import sys

input = sys.stdin.readline

N = int(input())
xy = []
for i in range(N):
    x, y = map(int, input().split())
    xy.append((i, x, y))

v = []

xy.sort(key=lambda x: x[1])
pi, px, py = xy[0]
for i in range(1, N):
    ci, cx, cy = xy[i]
    v.append((min(cx - px, abs(cy - py)), pi, ci))
    pi, px, py = ci, cx, cy

xy.sort(key=lambda x: x[2])
pi, px, py = xy[0]
for i in range(1, N):
    ci, cx, cy = xy[i]
    v.append((min(cy - py, abs(cx - px)), pi, ci))
    pi, px, py = ci, cx, cy


class UnionFind:
    def __init__(self, N):
        self.par = [-1] * N

    def root(self, x):
        while self.par[x] >= 0:
            x = self.par[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            if self.par[rx] > self.par[ry]:
                self.par[rx] = ry
            else:
                if self.par[rx] == self.par[ry]:
                    self.par[rx] -= 1
                self.par[ry] = rx

    def same(self, x, y):
        return self.root(x) == self.root(y)


uf = UnionFind(N)
counter = 0
s = 0

v.sort()
for v_ in v:
    c, a, b = v_
    if not uf.same(a, b):
        uf.unite(a, b)
        counter += 1
        s += c
        if counter == N - 1:
            break

print(s)
