N, K, L = map(int, input().split())

mod = 998244353

ret = 1

# (N-K)個前 ~ 1個前のと違うものを選ぶ
for i in range(N):
    if i <= N - K:
        ret *= max(L - i, 0)
    else:
        ret *= max(L - (N - K), 0)
    ret %= mod

print(ret)
