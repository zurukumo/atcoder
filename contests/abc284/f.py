N = int(input())
T = input()


class RollingHash:
    # mod ex. (1<<61)-1, (1<<31)-1
    # 文字列のときはxをordに通すのを忘れない！！
    def __init__(self, x, base=26, mod=(1 << 61) - 1):
        self.hash = [0]
        self.pow = [1]
        self.mod = mod

        for xi in x:
            self.hash.append((self.hash[-1] * base + xi) % mod)
            self.pow.append(self.pow[-1] * base % mod)

    # [l, r)
    def get(self, l, r):
        return (self.hash[r] - self.hash[l] * self.pow[r - l]) % self.mod

    def get2(self, l1, r1, l2, r2):
        return (self.get(l1, r1) * self.pow[r2 - l2] + self.get(l2, r2)) % self.mod


ordT = [ord(c) - ord("a") for c in T]

rh1 = RollingHash(ordT, base=26, mod=(1 << 61) - 1)
rh2 = RollingHash(ordT, base=26, mod=(1 << 31) - 1)
rrh1 = RollingHash(ordT[::-1], base=26, mod=(1 << 61) - 1)
rrh2 = RollingHash(ordT[::-1], base=26, mod=(1 << 31) - 1)


for i in range(N + 1):
    a = rh1.get2(0, i, N + i, 2 * N)
    b = rrh1.get(N - i, 2 * N - i)

    c = rh2.get2(0, i, N + i, 2 * N)
    d = rrh2.get(N - i, 2 * N - i)

    if a == b and c == d:
        print(T[:i] + T[N + i :])
        print(i)
        exit()

print(-1)
