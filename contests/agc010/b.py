N = int(input())
A = [int(i) for i in input().split()]


def solve():
    s = sum(A)
    if s % (N * (N + 1) // 2) != 0:
        return "NO"

    a = s // (N * (N + 1) // 2)
    ret = 0
    for i in range(N):
        d = A[i] - A[i - 1]
        if (a - d) % N != 0 or (a - d) < 0:
            return "NO"
        ret += (a - d) // N

    if ret == a:
        return "YES"
    else:
        return "NO"


print(solve())
