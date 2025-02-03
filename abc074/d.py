N = int(input())
A = [[int(i) for i in input().split()] for _ in range(N)]


def judge():
    s = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                if i == k or j == k:
                    continue
                if A[i][k] + A[k][j] < A[i][j]:
                    return -1
                elif A[i][k] + A[k][j] == A[i][j]:
                    s += A[i][j]
                    break
    tot = 0
    for i in range(N):
        for j in range(i + 1, N):
            tot += A[i][j]
    return tot - s


print(judge())
