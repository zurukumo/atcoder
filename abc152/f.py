N = int(input())
ab = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    ab[a - 1].append((b - 1, i))
    ab[b - 1].append((a - 1, i))
M = int(input())
uv = [[int(i) for i in input().split()] for _ in range(M)]

dp = [0] * M


def dfs(cur, pre, t, i):
    if cur == t:
        return True
    for nex, j in ab[cur]:
        if nex == pre:
            continue
        if dfs(nex, cur, t, i):
            dp[i] |= 1 << j
            return True
    return False


for i, (u, v) in enumerate(uv):
    dfs(u - 1, -1, v - 1, i)

ret = 1 << (N - 1)
for i in range(1, 1 << M):
    sgn = 1
    s = 0
    for j in range(M):
        if i & (1 << j):
            s |= dp[j]
            sgn *= -1
    ret += sgn * (1 << (N - 1 - bin(s).count("1")))

print(ret)
