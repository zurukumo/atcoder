N, W = map(int, input().split())
vw = [[int(i) for i in input().split()] for _ in range(N)]


def knapsack(i, w):
    if (i, w) in dp:
        return dp[(i, w)]

    if i == N:
        return 0
    elif w < vw[i][1]:
        ret = knapsack(i + 1, w)
    else:
        ret = max(knapsack(i + 1, w), knapsack(i + 1, w - vw[i][1]) + vw[i][0])

    dp[(i, w)] = ret
    return ret


# Case1: N<=30, 0<=v,w<=10^9
if N <= 30:
    dp = dict()
    print(knapsack(0, W))

else:
    Vmax = max([v for v, _ in vw])
    # Case2: N<=200, 0<=v<=10^9, 0<=w<=1000
    if Vmax > 1000:
        Wmax = max([w for _, w in vw])
        vw.sort(key=lambda x: x[1], reverse=True)
        dp = [-float("inf")] * (N * Wmax + 1)
        dp[0] = 0
        for i in range(N):
            for j in range(N * Wmax, vw[i][1] - 1, -1):
                dp[j] = max(dp[j], dp[j - vw[i][1]] + vw[i][0])
        print(max(dp[: W + 1]))

    # Case3: N<=200, 0<=v<=1000, 0<=w<=10^9
    else:
        vw.sort(key=lambda x: x[0], reverse=True)
        dp = [float("inf")] * (N * Vmax + 1)
        dp[0] = 0
        for i in range(N):
            for j in range(N * Vmax, vw[i][0] - 1, -1):
                dp[j] = min(dp[j], dp[j - vw[i][0]] + vw[i][1])
        M = 0
        for i in range(N * Vmax + 1):
            if dp[i] <= W:
                M = i
        print(M)
