N, K = map(int, input().split())
X = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

dp = [i - 1 for i in X]
if K % 2 == 1:
    A = [A[i] for i in dp]
K //= 2
for _ in range(60):
    dp = [dp[i] for i in dp]
    if K % 2 == 1:
        A = [A[i] for i in dp]
    K //= 2

print(*A)
