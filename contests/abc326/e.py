N = int(input())
A = [int(i) for i in input().split()]
mod = 998244353

s = 1
inv = pow(N, mod - 2, mod)
prob = [0] * N
for i in range(N):
    prob[i] = s * inv % mod
    s += prob[i]
    s %= mod

ret = 0
for i in range(N):
    ret += A[i] * prob[i]
    ret %= mod
print(ret)
