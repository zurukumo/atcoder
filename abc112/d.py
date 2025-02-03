N, M = map(int, input().split())


def solve():
    ret = 1
    i = 1
    while i * i <= M:
        if M % i == 0:
            if i >= N:
                ret = max(ret, M // i)
            if M // i >= N:
                ret = max(ret, i)
        i += 1

    return ret


print(solve())
