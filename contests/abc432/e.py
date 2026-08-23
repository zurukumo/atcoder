import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]


class SegTree:
    def __init__(self, n, v, f):
        i = 1
        while i < n:
            i <<= 1
        self.n = i
        self.v = v
        self.f = f
        self.tree = [v] * (i << 1)

    def update(self, i, x):
        i += self.n - 1
        self.tree[i] = x
        while i > 0:
            i = (i - 1) // 2
            self.tree[i] = self.f(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

    # [l, r)
    def query(self, l, r):
        l = l + self.n
        r = r + self.n
        s = self.v
        while l < r:
            if r & 1:
                r -= 1
                s = self.f(s, self.tree[r - 1])
            if l & 1:
                s = self.f(s, self.tree[l - 1])
                l += 1
            l >>= 1
            r >>= 1
        return s


stc = SegTree(5 * 10**5 + 1, 0, lambda x, y: x + y)
stv = SegTree(5 * 10**5 + 1, 0, lambda x, y: x + y)

counter = collections.Counter(A)
for k, v in counter.items():
    stc.update(k, v)
    stv.update(k, k * v)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, y = query
        x -= 1
        cur = stc.query(A[x], A[x] + 1)
        stc.update(A[x], cur - 1)
        stv.update(A[x], (cur - 1) * A[x])
        A[x] = y
        cur = stc.query(A[x], A[x] + 1)
        stc.update(A[x], cur + 1)
        stv.update(A[x], (cur + 1) * A[x])
    else:
        _, l, r = query
        if l >= r:
            print(l * N)
        else:
            a = stc.query(0, l)
            c = stc.query(r, 5 * 10**5 + 1)
            print(a * l + stv.query(l, r) + c * r)
