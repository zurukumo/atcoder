N = int(input())
h = [int(i) for i in input().split()]


def rec(h):
    m = min(h)
    for i in range(len(h)):
        h[i] -= m

    ret = m
    pre = 0
    for i in range(len(h)):
        if h[i] == 0:
            if i - pre > 0:
                ret += rec(h[pre:i])
            pre = i + 1
        elif i == len(h) - 1:
            ret += rec(h[pre:])
    return ret


print(rec(h))
