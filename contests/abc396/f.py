N, M = map(int, input().split())
A = [int(i) for i in input().split()]

A = [a % M for a in A]


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


ret = [0] * M
dec_fr = [0] * M
dec_to = [0] * M
inc_fr = [0] * M
inc_to = [0] * M
st = SegTree(M, 0, lambda x, y: x + y)
for i in range(N):
    a = A[i]
    ret[0] += st.query(a + 1, M)
    dec_to[a] += st.query(a + 1, M)
    inc_to[a] += st.query(0, a)
    st.update(a, st.query(a, a + 1) + 1)

st = SegTree(M, 0, lambda x, y: x + y)
for i in range(N - 1, -1, -1):
    a = A[i]
    dec_fr[a] += st.query(0, a)
    inc_fr[a] += st.query(a + 1, M)
    st.update(a, st.query(a, a + 1) + 1)


for i in range(1, M):
    ret[i] = ret[i - 1] - dec_fr[M - i] + inc_to[M - i] + dec_to[M - i] - inc_fr[M - i]

for r in ret:
    print(r)
