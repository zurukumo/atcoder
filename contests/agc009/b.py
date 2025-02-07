import sys

input = sys.stdin.readline

N = int(input())
v = [[] for _ in range(N)]
for i in range(N - 1):
    a = int(input())
    v[a - 1].append(i + 1)

l = [0]
i = 0
while i < len(l):
    cur = l[i]
    for nex in v[cur]:
        l.append(nex)
    i += 1

dp = [0] * N
while len(l) > 0:
    cur = l.pop()
    ret = []
    for nex in v[cur]:
        ret.append(dp[nex])

    if len(ret) == 0:
        continue

    ret.sort(reverse=True)
    dp[cur] = max([i + 1 + ret[i] for i in range(len(ret))])

print(dp[0])
