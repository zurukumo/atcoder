N, A, B, K = map(int, input().split())
mod = 998244353

fac = [1]
inv = [1]
for i in range(1, N + 1) :
    fac.append(fac[-1] * i % mod)
    inv.append(pow(fac[-1], mod - 2, mod))

ret = 0
for na in range(N + 1) :
    if (K - na * A) % B != 0 :
        continue
        
    nb = (K - na * A) // B
    if 0 <= na <= N and 0 <= nb <= N :
        ret += fac[N] * inv[N-na] * inv[na] * fac[N] * inv[N-nb] * inv[nb]
        ret %= mod
        
print(ret)
