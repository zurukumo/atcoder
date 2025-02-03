N, M = map(int, input().split())
A = [int(i) for i in input().split()]

need = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1] * (N + 10)
dp[0] = 0
for i in range(N) :
    if dp[i] < 0 :
        continue
        
    for j in A :
        dp[i+need[j]] = max(dp[i+need[j]], dp[i]*10+j)
        
print(dp[N])