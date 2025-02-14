N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]


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


st = SegTree(N, 0, max)

ab.sort(key=lambda x: x[0])

pre = -1
queue = []
for a, b in ab:
    a -= 1
    b -= 1
    if a != pre:
        while queue:
            old_b, v = queue.pop()
            st.update(old_b, v)

    queue.append((b, st.query(0, b) + 1))
    pre = a


while queue:
    old_b, v = queue.pop()
    st.update(old_b, v)

print(st.query(0, N))
