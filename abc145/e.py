import sys
input = sys.stdin.readline

N, T = map(int, input().split())
vw = [[int(i) for i in input().split()] for _ in range(N)]
vw.sort()

M = [0] * N
for i in range(N - 1, -1, -1) :
    M[i] = max(M[i], vw[i][1])
        
dp = [-float('inf')] * T
dp[0] = 0
ret = 0

for n, (w, v) in enumerate(vw) :
    for i in range(T-1, w-1, -1) :
        dp[i] = max(dp[i], dp[i-w]+v)
    
    if n + 1 < N :
        ret = max(ret, max(dp) + M[n + 1])
    else :
        ret = max(ret, max(dp))
    
print(ret)