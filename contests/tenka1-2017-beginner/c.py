N = int(input())


def solve():
    for a in range(1, 3501):
        for b in range(1, 3501):
            if 4 * a * b <= (a + b) * N:
                continue

            if a * b * N % (4 * a * b - (a + b) * N) == 0:
                return a, b, a * b * N // (4 * a * b - (a + b) * N)


print(*solve())
