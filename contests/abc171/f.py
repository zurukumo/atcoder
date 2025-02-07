K = int(input())
S = input()

mod = 10**9 + 7

N = len(S) + K

power = [1]
fac = [1]
inv = [1]
for i in range(1, N + 10):
    power.append(power[-1] * 25 % mod)
    fac.append(fac[-1] * i % mod)

inv = [pow(fac[-1], mod - 2, mod)]
for i in range(N + 10 - 1, 0, -1):
    inv.append(inv[-1] * i % mod)
inv = inv[::-1]


def comb(n, r):
    if r == 0:
        return 1
    return fac[n] * inv[n - r] * inv[r] % mod


ret = pow(26, N, mod)
for i in range(len(S)):
    ret -= power[N - i] * comb(N, i) % mod
    ret %= mod

print(ret)
