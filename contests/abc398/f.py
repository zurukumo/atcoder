S = input()


class RollingHash:
    # mod ex. (1<<61)-1, (1<<31)-1
    # 文字列のときはxをordに通すのを忘れない！！
    def __init__(self, x, base=65, mod=(1 << 61) - 1):
        self.hash = [0]
        self.pow = [1]
        self.mod = mod

        for xi in x:
            self.hash.append((self.hash[-1] * base + xi) % mod)
            self.pow.append(self.pow[-1] * base % mod)

    # [l, r)
    def get(self, l, r):
        return (self.hash[r] - self.hash[l] * self.pow[r - l]) % self.mod


l1 = RollingHash([ord(c) for c in S[::-1]], mod=(1 << 61) - 1)
r1 = RollingHash([ord(c) for c in S], mod=(1 << 61) - 1)
l2 = RollingHash([ord(c) for c in S[::-1]], mod=(1 << 31) - 1)
r2 = RollingHash([ord(c) for c in S], mod=(1 << 31) - 1)

N = len(S)
M = 0
for i in range(N + 1):
    if l1.get(0, i) == r1.get(N - i, N) and l2.get(0, i) == r2.get(N - i, N):
        M = max(M, i)


ret = S + S[:-M][::-1]
print(ret)
