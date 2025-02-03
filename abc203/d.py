N, K = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]


def judge(m):
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for y in range(N):
        for x in range(N):
            if A[y][x] <= m:
                dp[y + 1][x + 1] = 1
            else:
                dp[y + 1][x + 1] = -1

    # print('m', m)
    # for dp_ in dp:
    # print(dp_)
    # print('======')

    for y in range(N + 1):
        for x in range(N + 1):
            if y >= 1:
                dp[y][x] += dp[y - 1][x]
            if x >= 1:
                dp[y][x] += dp[y][x - 1]
            if y >= 1 and x >= 1:
                dp[y][x] -= dp[y - 1][x - 1]

    # for dp_ in dp:
    # print(dp_)
    # print()

    for y in range(K, N + 1):
        for x in range(K, N + 1):
            if dp[y][x] - dp[y - K][x] - dp[y][x - K] + dp[y - K][x - K] >= 0:
                # print('True')
                return True

    # print('False')
    return False


ng, ok = -1, 10**9 + 10
while ok - ng > 1:
    m = (ok + ng) // 2

    if judge(m):
        ok = m
    else:
        ng = m

    # print(ok, ng)

print(ok)
