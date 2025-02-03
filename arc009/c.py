N, K = map(int, input().split())
mod = 1777777777

ret = 0
fac = 1
inv = 1
sgn = 1
for i in range(1, K + 1):
    fac = fac * i % mod
    inv = pow(fac, mod - 2, mod)
    if i != 1:
        ret += sgn * inv
        ret %= mod
        sgn *= -1

for i in range(K):
    ret *= N - i
    ret %= mod

print(ret)
