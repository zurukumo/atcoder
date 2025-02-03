N, M = map(int, input().split())

vec = [[] for _ in range(N)]
for _ in range(M) :
    x, y = map(int, input().split())
    vec[x-1].append(y-1)
    
dp = [0] * (1 << N)
dp[0] = 1

for i in range(1 << N) :
    for j in range(N) :
        if (i >> j) & 1 :
            continue
        
        flag = True
        for k in vec[j] :
            if (i >> k) & 1 :
                flag = False
        
        if flag :
            dp[i|(1 << j)] += dp[i]
            
print(dp[-1])