N = int(input())

v = [[] for _ in range(N)]

for i in range(1, N):
    b = int(input()) - 1
    v[b].append(i)


def bfs(i):
    M, m = 0, float("inf")
    if len(v[i]) == 0:
        return 1

    for j in v[i]:
        s = bfs(j)
        M = max(M, s)
        m = min(m, s)
    return M + m + 1


print(bfs(0))
