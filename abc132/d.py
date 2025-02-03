N, K = map(int, input().split())

if N == 1 and K == 1 :
    print(1)
else :

    MOD = 10 ** 9 + 7

    M = max(K-1, N-K+1)

    fac = [0] * (M + 1)
    inv = [0] * (M + 1)
    fac[0] = 1
    inv[0] = 1

    for i in range(1, M + 1) :
        fac[i] = fac[i-1] * i
        inv[i] = pow(fac[i], MOD - 2, MOD)
        
    def comb(n, r) :
        if n <= 0 :
            return 0
        if r > n :
            return 0
            
        return fac[n]*inv[n-r]*inv[r]%MOD
        
    for i in range(1, K + 1) :
        print(comb(K-1, i-1) * comb(N-K+1, i) % MOD)