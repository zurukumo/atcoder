n = int(input())
k = int(input())
MOD = 10 ** 9 + 7

fac = [0] * (n + k)
inv = [0] * (n + k)
fac[0] = 1
inv[0] = 1
for i in range(1, n + k) :
    fac[i] = i * fac[i-1] % MOD
    inv[i] = pow(fac[i], MOD - 2, MOD)

print(fac[n+k-1] * inv[n-1] * inv[k] % MOD)
    