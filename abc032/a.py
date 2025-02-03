a = int(input())
b = int(input())
n = int(input())

def gcd(m, n) :
    if n > m :
        m, n = n, m
        
    while m % n != 0 :
        m, n = n, m % n
        
    return n
        
def lcm(m, n) :
    return m * n // gcd(m, n)
    
l = lcm(a, b)
print(-(-n//l) * l)