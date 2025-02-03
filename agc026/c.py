from collections import defaultdict

N = int(input())
S = input()

T = [ord(S[i]) - 96 for i in range(N)]
U = [ord(S[i]) - 96 for i in range(2*N-1, N-1, -1)]


c1 = defaultdict(int)
c2 = defaultdict(int)

for i in range(1 << N) :
    a1, a2, b1, b2 = 0, 0, 0, 0
    for j in range(N) :
        if i & 1 :
            a1 = a1 * 27 + T[j]
            b1 = b1 * 27 + U[j]
        else :
            a2 = a2 * 27 + T[j]
            b2 = b2 * 27 + U[j]
        i >>= 1
        
    c1[(a1, a2)] += 1
    c2[(b1, b2)] += 1

ret = 0
for k, v in c1.items() :
    ret += v * c2[k]
print(ret)