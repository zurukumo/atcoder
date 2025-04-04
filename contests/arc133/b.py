N = int(input())
P = [int(i) for i in input().split()]
Q = [int(i) for i in input().split()]

ppos = [0] * (N + 1)
qpos = [0] * (N + 1)
for i, (p, q) in enumerate(zip(P, Q)):
    ppos[p] = i
    qpos[q] = i


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


st = SegTree(N + 1, 0, max)
ret = 0
for i in range(N):
    p = P[i]
    queue = []
    for multiple in range(p, N + 1, p):
        j = qpos[multiple]
        v = st.query(0, j) + 1
        queue.append((j, v))
        ret = max(ret, v)
    for j, v in queue:
        st.update(j, v)

print(ret)
