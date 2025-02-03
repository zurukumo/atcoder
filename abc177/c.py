N = int(input())
A = [int(i) for i in input().split()]

mod = 10**9 + 7

sum = [0] * N
A = A[::-1]
sum[0] = A[0]
for i in range(1, N):
    sum[i] = (sum[i - 1] + A[i]) % mod

sum = sum[::-1]
A = A[::-1]

ret = 0
for i in range(N - 1):
    ret += A[i] * sum[i + 1] % mod
    ret %= mod

print(ret)
