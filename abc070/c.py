N = int(input())
T = [int(input()) for _ in range(N)]

def gcd(m, n) :
    if m < n :
        m, n = n, m
        
    while n != 0 :
        m, n = n, m % n
    return m

ret = 1
for i in range(N) :
    ret = ret * T[i] // gcd(ret, T[i])
    
print(ret)