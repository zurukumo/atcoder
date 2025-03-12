N, M, K = map(int, input().split())

mod = 998244353

if N == 1 and M == 1:
    print(K)
    exit()

if N == 1:
    print(pow(K, M, mod))
    exit()

if M == 1:
    print(pow(K, N, mod))
    exit()


ret = 0
for k in range(1, K + 1):
    ret += pow(k, N, mod) * (pow(K - k + 1, M, mod) - pow(K - k, M, mod)) % mod
    ret %= mod

print(ret)
