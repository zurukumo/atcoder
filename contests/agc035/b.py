import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())

if M % 2 == 0:
    vec = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        vec[A - 1].append(B - 1)
        vec[B - 1].append(A - 1)

    visited = [False] * N
    CD = [[] for _ in range(N)]

    def dfs(cur, pre):
        for nex in vec[cur]:
            if nex == pre:
                continue

            if not visited[nex]:
                visited[nex] = True
                dfs(nex, cur)
            elif not cur in CD[nex]:
                CD[cur].append(nex)

        if pre != -1:
            if len(CD[cur]) % 2 == 0:
                CD[pre].append(cur)
            else:
                CD[cur].append(pre)

    visited[0] = True
    dfs(0, -1)

    for i in range(N):
        for j in CD[i]:
            print(i + 1, j + 1)
else:
    print(-1)
