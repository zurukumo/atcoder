N, M = map(int, input().split())
dp = [False] * N
dp[0] = True
count = [1] * N
for _ in range(M) :
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    dp[y] |= dp[x]
    count[x] -= 1
    count[y] += 1
    if count[x] == 0 :
        dp[x] = False
    
ret = 0
for i in range(N) :
    if dp[i] and count[i] > 0 :
        ret += 1
print(ret)