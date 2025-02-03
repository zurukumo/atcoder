from collections import Counter
N, M = map(int, input().split())

if M == 1 :
    print(1)

else :
    mod = 10 ** 9 + 7

    fac = [1]
    inv = [1]
    for i in range(1, N + 1) :
        fac.append(fac[-1] * i % mod)
        inv.append(pow(fac[-1], mod - 2, mod))

    def rec(m, pre_divisor, divisors, lev) :
        ret = 0
        if lev == N :
            comb = fac[N]
            for c in Counter(divisors + [m]).values() :
                comb *= inv[c]
                comb %= mod
            ret += comb
            ret %= comb
            return ret
        
        i = pre_divisor
        while i * i <= m :
            if m % i == 0 :
                ret += rec(m // i, i, divisors + [i], lev + 1)
            i += 1
        
        comb = fac[N]
        for c in Counter(divisors + [m]).values() :
            comb *= inv[c]
            comb %= mod
        comb *= inv[N-lev-1]
        comb %= mod
        ret += comb
        ret %= mod
        return ret
        
    print(rec(M, 2, [], 0))