N = int(input())
mod = 10 ** 9 + 7

if N < 3 :
    print(0)
else :
    # A0 G1 C2 T3
    # AGC,ACG,GACはすぐ消す
    # AGx,AxGにはCを足しちゃいけないことにする
    
    dp = [1] * 64
    dp[6] = dp[9] = dp[18] = 0
     
    for _ in range(N-3) :
        dp_ = [0] * 64
        for i in range(64) :
            for j in range(4) :
                if j == 2 and i in [1, 4, 5, 7, 13] :
                    continue
                ni = (i*4+j)%64
                dp_[ni] += dp[i]
                dp_[ni] %= mod
        dp = dp_
        dp[6] = dp[9] = dp[18] = 0
        
    print(sum(dp) % mod)