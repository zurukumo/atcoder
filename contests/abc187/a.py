A, B = input().split()


def f(s):
    ret = 0
    for c in s:
        ret += int(c)
    return ret


print(max(f(A), f(B)))
