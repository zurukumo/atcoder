H, W, A, B = map(int, input().split())
MOD = 10 ** 9 + 7

fac = [1]
inv = [1]

for i in range(1, H+W+1) :
    fac.append(fac[-1] * i % MOD)
    inv.append(pow(fac[-1], MOD - 2, MOD))
    
ret = 0
for i in range(H-A) :
    ret += fac[i+B-1]*inv[i]*inv[B-1]*fac[H+W-i-B-2]*inv[H-i-1]*inv[W-B-1]%MOD
    ret %= MOD
    
print(ret)