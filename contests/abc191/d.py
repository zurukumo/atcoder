X, Y, R = map(float, input().split())
E = 10**4
X = int(round(X * E))
Y = int(round(Y * E))
R = int(round(R * E))


def isqrt(x):
    l, r = 0, x
    while r - l > 1:
        m = (l + r) // 2
        if m * m > x:
            r = m
        else:
            l = m
    return l


ret = 0
for x in range(-R + X + (R - X) % E, R + X + 1, E):
    root = isqrt(R**2 - (x - X) ** 2)
    l = Y - root
    r = Y + root
    l += (-l) % E
    r -= r % E

    ret += max(0, (r - l) // E + 1)

print(ret)
