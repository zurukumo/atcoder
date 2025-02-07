Y, M, D = map(int, input().split("/"))


def is_leap(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False


def solve(Y, M, D):
    while True:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leap(Y):
            month[1] = 29

        for m in range(M, 12 + 1):
            for d in range(D, month[m - 1] + 1):
                if Y % (m * d) == 0:
                    return "{:02}/{:02}/{:02}".format(Y, m, d)
            D = 1
        M = 1
        Y += 1


print(solve(Y, M, D))
