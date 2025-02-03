N = int(input())
C = [int(i) for i in input().split()]
mod = 10**9 + 7

C.sort()

ret = 0
P = pow(4, N - 1, mod)
for i in range(N):
    ret += C[i] * P * (N - i + 1) % mod
    ret %= mod

print(ret)
