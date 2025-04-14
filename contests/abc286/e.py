import collections

N = int(input())
A = [int(i) for i in input().split()]
S = [input() for _ in range(N)]
Q = int(input())
UV = [[int(i) for i in input().split()] for _ in range(Q)]

dp = [[[float("inf"), -float("inf")] for _ in range(N)] for _ in range(N)]
for i in range(N):
    dp[i][i][1] = A[i]

for s in range(N):
    queue = collections.deque([(s, 0, A[s])])
    while queue:
        cur, cost, value = queue.popleft()
        if dp[s][cur][0] < cost:
            continue
        if dp[s][cur][1] > value:
            continue
        for nex in range(N):
            if S[cur][nex] == "Y" and dp[s][nex][0] >= cost + 1 and dp[s][nex][1] < value + A[nex]:
                queue.append((nex, cost + 1, value + A[nex]))
                dp[s][nex][0] = cost + 1
                dp[s][nex][1] = value + A[nex]

for u, v in UV:
    u -= 1
    v -= 1
    if dp[u][v][0] == float("inf"):
        print("Impossible")
    else:
        print(*dp[u][v])
