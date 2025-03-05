N, Q = map(int, input().split())
S = input()
query = [[int(i) for i in input().split()] for _ in range(Q)]


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


st = SegTree(N, 0, lambda x, y: x + y)

for i in range(N - 1):
    if S[i] != S[i + 1]:
        st.update(i, 1)

for type, l, r in query:
    l -= 1
    r -= 1
    if type == 1:
        if l - 1 >= 0:
            lv = st.query(l - 1, l)
            st.update(l - 1, 1 ^ lv)
        if r + 1 <= N:
            rv = st.query(r, r + 1)
            st.update(r, 1 ^ rv)
    else:
        if st.query(l, r) == r - l:
            print("Yes")
        else:
            print("No")
