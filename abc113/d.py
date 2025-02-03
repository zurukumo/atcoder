H, W, K = map(int, input().split())

mod = 10 ** 9 + 7

dp = [0] * W
dp[0] = 1

pattern = []
for i in range(1 << (W - 1)) :
    if '11' in bin(i) :
        continue
    pattern.append(i)

for _ in range(H) :
    dp_ = [0] * W
    for p in pattern :
        for i in range(W) :
            if i != W - 1 and p & (1 << i) :
                dp_[i+1] += dp[i]
                dp_[i+1] %= mod
            elif i != 0 and p & (1 << (i - 1)) :
                dp_[i-1] += dp[i]
                dp_[i-1] %= mod
            else :
                dp_[i] += dp[i]
                dp_[i] %= mod
    
    dp = dp_
    
print(dp[K-1])