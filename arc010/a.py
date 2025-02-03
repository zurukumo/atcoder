N, M, A, B = map(int, input().split())
c = [int(input()) for _ in range(M)]


def solve(N):
    if N <= A:
        N += B
    for i in range(M):
        if N < c[i]:
            return i + 1
        N -= c[i]
        if N <= A:
            N += B
    return "complete"


print(solve(N))
