N, M = map(int, input().split())


def solve():
    b = 0
    for b in range(N + 1):
        if (4 * N - b - M) % 2 != 0:
            continue
        a = (4 * N - b - M) // 2
        c = N - a - b

        if 0 <= a <= N and 0 <= b <= N and 0 <= c <= N:
            return (a, b, c)

    return (-1, -1, -1)


print(*solve())
