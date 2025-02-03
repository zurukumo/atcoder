L, R = map(int, input().split())

mod = 10 ** 9 + 7

dp = [[[0] * 2 for _ in range(2)] for _ in range(2)]
dp[0][0][0] = 1

for i in range(60, -1, -1) :
    lb, rb = (L >> i) & 1, (R >> i) & 1
    dp_ = [[[0] * 2 for _ in range(2)] for _ in range(2)]
    for lf in range(2) :
        for rf in range(2) :
            for msb in range(2) :
                for l in range(2) :
                    for r in range(2) :
                        nlf, nrf, nmsb = lf, rf, msb
                        if l > r : continue
                        if not msb and l != r : continue
                        if l and r :
                            nmsb = 1
                        if not lf and l < lb : continue
                        if l > lb :
                            nlf = 1
                        if not rf and r > rb : continue
                        if r < rb :
                            nrf = 1
                        dp_[nlf][nrf][nmsb] += dp[lf][rf][msb]
                        dp_[nlf][nrf][nmsb] %= mod
    dp = dp_
    
ret = 0
for i in range(2) :
    for j in range(2) :
        for k in range(2) :
            ret += dp[i][j][k]
            
print(ret % mod)