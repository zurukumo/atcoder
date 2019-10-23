# 素因数分解
def prime_factor(n) :
    ret = dict()
    if n % 2 == 0 :
        ret[2] = 0
        while n % 2 == 0 :
            n //= 2
            ret[2] += 1
            
    i = 3
    while i * i <= n :
        if n % i == 0 :
            ret[i] = 0
            
            while n % i == 0 :
                n //= i
                ret[i] += 1
        i += 2
        
    if n != 1 :
        ret[n] = 1
    
    return ret