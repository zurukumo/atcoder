from collections import defaultdict

A, B = map(int, input().split())
mod = 10 ** 9 + 7

factor = defaultdict(int)

def prime_factor(ret, n) :
    if n % 2 == 0 :
        while n % 2 == 0 :
            n //= 2
            ret[2] += 1
            
    i = 3
    while i * i <= n :
        if n % i == 0 :            
            while n % i == 0 :
                n //= i
                ret[i] += 1
        i += 2
        
    if n != 1 :
        ret[n] += 1
    
for i in range(B + 1, A + 1) :
    prime_factor(factor, i)
    
ret = 1
for v in factor.values() :
    ret *= v + 1
    ret %= mod
print(ret)