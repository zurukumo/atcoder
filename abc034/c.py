W, H = map(int, input().split())
MOD = 10 ** 9 + 7

W -= 1
H -= 1

fac = [0] * (W + H + 1)
inv = [0] * (W + H + 1)
fac[0] = 1
inv[0] = 1

for i in range(1, W+H+1) :
    fac[i] = i * fac[i-1] % MOD
    inv[i] = pow(fac[i], MOD-2, MOD)

print(fac[W+H]*inv[W]*inv[H]%MOD)