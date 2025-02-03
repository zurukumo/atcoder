A, B = map(int, input().split())


def f(x):
    ret = 0
    b = 1
    for i in range(44):
        c = (x // (b * 2)) * b
        rest = x % (b * 2)
        if rest - b > 0:
            c += rest - b
        if c & 1:
            ret += 1 << i
        b <<= 1
    return ret


print(f(A) ^ f(B + 1))
