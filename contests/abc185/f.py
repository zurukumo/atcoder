N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
TXY = [[int(i) for i in input().split()] for _ in range(Q)]


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


st = SegTree(N, 0, lambda x, y: x ^ y)
for i, a in enumerate(A):
    st.update(i, a)


for t, x, y in TXY:
    x -= 1
    if t == 1:
        st.update(x, st.query(x, x + 1) ^ y)
    else:
        y -= 1
        print(st.query(x, y + 1))
