import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
query = [[int(i) for i in input().split()] for _ in range(Q)]


class SegTree:
    def __init__(self, n, f):
        i = 1
        while i < n:
            i <<= 1
        self.n = i
        self.v = (0, 0, 0, 0)
        self.f = f
        self.tree = [(0, 0, 0, 0)] * (i << 1)

    def update(self, i, x):
        i += self.n - 1
        self.tree[i] = (x, 1, 0, 0)
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


def second_max(x, y):
    m1v, m1c, m2v, m2c = x
    for i in range(0, 4, 2):
        v, c = y[i], y[i + 1]
        if v > m1v:
            m1v, m2v = v, m1v
            m1c, m2c = c, m1c
        elif v == m1v:
            m1c += c
        elif m1v > v > m2v:
            m2v = v
            m2c = c
        elif v == m2v:
            m2c += c
    return m1v, m1c, m2v, m2c


st = SegTree(N, lambda x, y: second_max(x, y))

for i, a in enumerate(A):
    st.update(i, a)

for a, b, c in query:
    if a == 1:
        p, x = b - 1, c
        st.update(p, x)
    else:
        l, r = b - 1, c - 1
        _, _, _, m2c = st.query(l, r + 1)
        print(m2c)
