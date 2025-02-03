N, M, E = map(int, input().split())
UV = [[int(i) for i in input().split()] for _ in range(E)]
Q = int(input())
X = [int(input()) for _ in range(Q)]


class UnionFind:
    def __init__(self, N, M):
        self.parent = [-1] * (N + M)
        self.cnts = [1] * (N + M)
        self.connected = [False] * N + [True] * M
        self.s = 0

    def root(self, x):
        while self.parent[x] >= 0:
            x = self.parent[x]
        return x

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if rx != ry:
            if self.parent[rx] > self.parent[ry]:
                if self.connected[rx] and not self.connected[ry]:
                    self.s += self.size(ry)
                    self.connected[ry] = True
                elif self.connected[ry] and not self.connected[rx]:
                    self.s += self.size(rx)
                self.parent[rx] = ry
                self.cnts[ry] += self.cnts[rx]
            else:
                if self.connected[rx] and not self.connected[ry]:
                    self.s += self.size(ry)
                elif self.connected[ry] and not self.connected[rx]:
                    self.s += self.size(rx)
                    self.connected[rx] = True
                if self.parent[rx] == self.parent[ry]:
                    self.parent[rx] -= 1
                self.parent[ry] = rx
                self.cnts[rx] += self.cnts[ry]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return self.cnts[self.root(x)]


uf = UnionFind(N, M)
ret = []
yet = set(x - 1 for x in X)

for i, (u, v) in enumerate(UV):
    if not i in yet:
        uf.unite(u - 1, v - 1)

for x in reversed(X):
    x -= 1
    ret.append(uf.s)
    u, v = UV[x]
    uf.unite(u - 1, v - 1)

for i in reversed(ret):
    print(i)
