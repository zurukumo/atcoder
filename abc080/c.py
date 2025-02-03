from itertools import product

N = int(input())
F = [[int(i) for i in input().split()] for _ in range(N)]
P = [[int(i) for i in input().split()] for _ in range(N)]

M = -float('inf')
for open in product([0, 1], repeat=10) :
    if sum(open) == 0 :
        continue
        
    ret = 0
    for i in range(N) :
        ret += P[i][sum([F[i][j] & open[j] for j in range(10)])]
    M = max(M, ret)
print(M)