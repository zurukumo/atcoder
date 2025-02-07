R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

mod = 10**9 + 7

fac = [1]
inv = [1]
for i in range(1, R * C + 1):
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))


def comb(n, r):
    if n < 0 or n < r:
        return 0
    return fac[n] * inv[n - r] * inv[r] % mod


P1 = comb(X * Y, D) * comb(X * Y - D, L)
P2 = comb((X - 1) * Y, D) * comb((X - 1) * Y - D, L) * 2
P3 = comb(X * (Y - 1), D) * comb(X * (Y - 1) - D, L) * 2
P4 = comb((X - 2) * Y, D) * comb((X - 2) * Y - D, L)
P5 = comb(X * (Y - 2), D) * comb(X * (Y - 2) - D, L)
P6 = comb((X - 1) * (Y - 1), D) * comb((X - 1) * (Y - 1) - D, L) * 4
P7 = comb((X - 2) * (Y - 1), D) * comb((X - 2) * (Y - 1) - D, L) * 2
P8 = comb((X - 1) * (Y - 2), D) * comb((X - 1) * (Y - 2) - D, L) * 2
if X == Y == 1:
    P9 = 0
else:
    P9 = comb((X - 2) * (Y - 2), D) * comb((X - 2) * (Y - 2) - D, L)

ret = (
    (R - X + 1) * (C - Y + 1) * (P1 - (P2 + P3) + (P4 + P5 + P6) - (P7 + P8) + P9) % mod
)
print(ret)
