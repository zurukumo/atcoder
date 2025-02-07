from heapq import heappush, heappop

N, K = map(int, input().split())
P = [int(i) for i in input().split()]

dp = [0] * N
dp[0] = 1
for i in range(1, N):
    if P[i] > P[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = 1

ma = []
mi = []

for i in range(K):
    heappush(ma, (-P[i], i))
    heappush(mi, (P[i], i))

if dp[K - 1] == K:
    ret = 0
else:
    ret = 1

for i in range(K, N):
    heappush(ma, (-P[i], i))
    heappush(mi, (P[i], i))

    while ma[0][1] < i - K:
        heappop(ma)
    while mi[0][1] < i - K:
        heappop(mi)

    if dp[i] < K and (P[i - K] != mi[0][0] or P[i] != -ma[0][0]):
        ret += 1

if sum([dp[i] >= K for i in range(N)]) > 0:
    ret += 1

print(ret)
