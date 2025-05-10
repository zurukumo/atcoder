N, M = map(int, input().split())
uv = [[int(i) for i in input().split()] for _ in range(M)]

graph = [[] for _ in range(N)]
for u, v in uv:
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)


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


remove = set()
not_connected = []
uf = UnionFind(N)

for u in range(N):
    if u in remove:
        remove.remove(u)
    for v in graph[u]:
        if v > u:
            remove.add(v)
        elif v < u:
            uf.unite(u, v)

    not_connected.append(u)
    while not_connected and uf.same(0, not_connected[-1]):
        not_connected.pop()

    if len(not_connected) == 0:
        print(len(remove))
    else:
        print(-1)
