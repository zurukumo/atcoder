N, X = map(int, input().split())


def rec(level, X):
    if level == 0:
        return 1

    if X == 1:
        return 0

    elif X <= 2 ** (level + 1) - 2:
        return rec(level - 1, X - 1)

    elif X == 2 ** (level + 1) - 1:
        return 2**level

    elif X <= 2 ** (level + 2) - 4:
        return 2**level + rec(level - 1, X - (2 ** (level + 1) - 1))

    else:
        return 1 + (2**level - 1) * 2


print(rec(N, X))
