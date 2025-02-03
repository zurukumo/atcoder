N, K = map(int, input().split())
a = [int(i) for i in input().split()]

dp = [0] * (N + 1)
for i in range(N) :
    dp[i+1] = dp[i] + a[i]

ret = 0
prev_j = 1
for i in range(1, N+1) :
    for j in range(prev_j, N+1) :
        if dp[j] - dp[i-1] >= K :
            ret += N - j + 1
            prev_j = j
            break
            
print(ret)