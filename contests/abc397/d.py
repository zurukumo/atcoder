N = int(input())


def is_sqrt(x):
    l = 0
    r = x
    while r - l > 1:
        m = (r + l) // 2
        if m * m > x:
            r = m
        else:
            l = m
    return l, l * l == x


for i in range(1, 10**6 + 1):
    if N % i != 0:
        continue

    j = N // i
    a = 12 * j - 3 * i * i
    b, flag = is_sqrt(a)
    if flag and (-3 * i + b) % 6 == 0:
        y = (-3 * i + b) // 6
        x = i + y
        if x <= 0 or y <= 0:
            continue
        print(x, y)
        exit()

print(-1)
