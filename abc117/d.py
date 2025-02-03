N, K = map(int, input().split())
A = [int(i) for i in input().split()]

M = len(bin(K)) - 2
one = [0] * M
for i in range(N) :
    for j in range(M) :
        one[j] += (A[i] >> j) & 1 

X = 0
for i in range(M - 1, -1, -1) :
    X *= 2
    if N - one[i] > one[i] :
        X += 1
        
for i in range(M - 1, -1, -1) :
    a = (X >> i) & 1
    b = (K >> i) & 1
    if a == 0 and b == 1 :
        break
    if a == 1 and b == 0 :
        X ^= (1 << i)
        
ret = 0
for i in range(N) :
    ret += A[i] ^ X
print(ret)