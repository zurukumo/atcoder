N, M = map(int, input().split())
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


dp = [A[0] % M]
for i in range(1, N):
    dp.append((dp[-1] + A[i]) % M)

ret = 0
vst = SegTree(M + 1, 0, lambda x, y: x + y)
cst = SegTree(M + 1, 0, lambda x, y: x + y)
vst.update(0, 0)
cst.update(0, 1)
for i in range(N):
    ret += dp[i] * cst.query(0, dp[i]) - vst.query(0, dp[i])
    ret += (dp[i] + M) * cst.query(dp[i] + 1, M + 1) - vst.query(dp[i] + 1, M + 1)
    vst.update(dp[i], vst.query(dp[i], dp[i] + 1) + dp[i])
    cst.update(dp[i], cst.query(dp[i], dp[i] + 1) + 1)

print(ret)
