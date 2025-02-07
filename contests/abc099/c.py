import sys

sys.setrecursionlimit(10**5)

N = int(input())


def rec(N, m):
    if N < 6:
        return N + m

    a, b = float("inf"), float("inf")
    six = 6
    while six * 6 <= N:
        six *= 6
    if N >= six:
        a = rec(N - six, m + 1)

    nine = 9
    while nine * 9 <= N:
        nine *= 9
    if N >= nine:
        b = rec(N - nine, m + 1)

    return min(a, b)


print(rec(N, 0))
