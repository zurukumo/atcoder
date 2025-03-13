import bisect

N, S = map(int, input().split())
A = [int(i) for i in input().split()]

sumA = [0] * N
sumA[0] = A[0]
for i in range(1, N):
    sumA[i] = sumA[i - 1] + A[i]

dp = [1] * N
for i in range(N):
    if i - 1 >= 0:
        j = bisect.bisect_left(sumA, sumA[i - 1] + S + 1)
    else:
        j = bisect.bisect_left(sumA, S + 1)
    if j < N:
        dp[j] += dp[i]

print(sum(dp[i] * (N - i) for i in range(N)))
