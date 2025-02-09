N, Q = map(int, input().split())
P = [input() for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if P[i][j] == "B":
            dp[i][j] = 1

for i in range(N):
    for j in range(N):
        if i > 0:
            dp[i][j] += dp[i - 1][j]
        if j > 0:
            dp[i][j] += dp[i][j - 1]
        if i > 0 and j > 0:
            dp[i][j] -= dp[i - 1][j - 1]


def square(a, b):
    if a < 0 or b < 0:
        return 0
    return dp[a][b]


def big_square(a, b):
    if a < 0 or b < 0:
        return 0

    s = 0
    na = (a + 1) - (a + 1) % N - 1
    nb = (b + 1) - (b + 1) % N - 1
    s += (na + 1) * (nb + 1) // N // N * square(N - 1, N - 1)
    if a % N != N - 1:
        s += square(a % N, N - 1) * (nb + 1) // N
    if b % N != N - 1:
        s += square(N - 1, b % N) * (na + 1) // N
    if a % N != N - 1 and b % N != N - 1:
        s += square(a % N, b % N)
    return s


for _ in range(Q):
    A, B, C, D = map(int, input().split())

    ret = 0
    ret += big_square(C, D)
    ret -= big_square(A - 1, D)
    ret -= big_square(C, B - 1)
    ret += big_square(A - 1, B - 1)

    print(ret)
