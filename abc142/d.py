A, B = map(int, input().split())

def gcd(m, n) :
    while n :
        m, n = n, m % n
    return m

ret = 0
x = gcd(A, B)
if x % 2 == 0 :
    ret += 1
    while x % 2 == 0 :
        x //= 2
        
i = 3
while i * i <= x :
    if x % i == 0 :
        ret += 1
        x //= i
        
    while x % i == 0 :
        x //= i
        
    i += 2

if x != 1 :
    ret += 1
print(ret + 1)
