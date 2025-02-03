N = int(input())
A = [int(i) for i in input().split()]

def gcd(m, n) :
    if m < n :
        m, n = n, m
    while m % n :
        m, n = n, m % n
    return n

gcdL = [0] * N
gcdR = [0] * N
gcdL[0] = A[0]
gcdR[N-1] = A[N-1]

for i in range(1, N) :
    gcdL[i] = gcd(gcdL[i-1], A[i])
    gcdR[N-1-i] = gcd(gcdR[N-i], A[N-1-i])
  
ret = max(gcdL[N-2], gcdR[1])
for i in range(1, N - 1) :
    ret = max(ret, gcd(gcdL[i-1], gcdR[i+1]))

print(ret)