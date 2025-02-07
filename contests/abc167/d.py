N, K = map(int, input().split())
A = [int(i) - 1 for i in input().split()]


def solve():
    global K
    visited = [-1] * N
    visited[0] = 0

    cur = 0
    while True:
        nex = A[cur]
        if visited[cur] == K - 1:
            return nex + 1

        if visited[nex] == -1:
            visited[nex] = visited[cur] + 1
            cur = nex
        else:
            # 一回目
            i = visited[nex]
            # 二回目
            j = visited[cur] + 1
            K -= i
            K %= j - i
            cur = nex
            break

    while K > 0:
        cur = A[cur]
        K -= 1

    return cur + 1


print(solve())
