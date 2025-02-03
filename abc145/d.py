X, Y = map(int, input().split())
mod = 10 ** 9 + 7

if (X + Y) % 3 == 0 : 
    n = (X + Y) // 3
    a = 2 * n - X
    
    if 0 <= a <= n and a * 2 + (n - a) == Y :
        fac = [1]
        inv = [1]
        for i in range(1, n + 1) :
            fac.append(fac[-1] * i % mod)
            inv.append(pow(fac[-1], mod - 2, mod))
        print(fac[n] * inv[n-a] * inv[a] % mod)
    
    else :
        print(0)
        
else :
    print(0)