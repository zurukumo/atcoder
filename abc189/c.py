N = int(input())
A = [int(i) for i in input().split()]


class UnionFind:
    def __init__(self, N):
        self.parent = [-1] * N
        self.s = [1] * N

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
                self.s[ry] += self.s[rx]
            else:
                if self.parent[rx] == self.parent[ry]:
                    self.parent[rx] -= 1
                self.parent[ry] = rx
                self.s[rx] += self.s[ry]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return self.s[self.root(x)]


UF = UnionFind(N)
AA = [(a, i) for i, a in enumerate(A)]
AA.sort(reverse=True)
ret = -float("inf")
done = [False] * N

for a, i in AA:
    l = max(0, i - 1)
    r = min(N - 1, i + 1)

    if done[l]:
        UF.unite(l, i)
    if done[r]:
        UF.unite(r, i)
    done[i] = True
    ret = max(ret, a * UF.size(i))

print(ret)
