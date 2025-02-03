a, b, k = map(int, input().split())


def comb(n, k):
    ret = 1
    for i in range(1, n + 1):
        ret *= i
    for i in range(1, k + 1):
        ret //= i
    for i in range(1, n - k + 1):
        ret //= i
    return ret


ret = ""
for _ in range(a + b):
    if a == 0:
        ret += "b"
        b -= 1
    elif b == 0:
        a -= 1
        ret += "a"
    else:
        if k <= comb(a + b - 1, b):
            ret += "a"
            a -= 1
        else:
            ret += "b"
            k -= comb(a + b - 1, b)
            b -= 1
print(ret)
