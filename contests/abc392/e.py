N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]


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
rest = []
for i, (a, b) in enumerate(AB):
    a -= 1
    b -= 1
    if uf.same(a, b):
        rest.append((i, a, b))
    else:
        uf.unite(a, b)

ps = set([i for i in range(N) if uf.parents[i] < 0])
print(len(ps) - 1)
while len(ps) > 1:
    i, a, b = rest.pop()
    for x in ps:
        if not uf.same(a, x):
            uf.unite(a, x)
            ps.remove(x)
            print(i + 1, b + 1, x + 1)
            break
