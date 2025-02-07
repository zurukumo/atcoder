y = int(input())
m = int(input())
d = int(input())


def f(y, m, d):
    if m == 1 or m == 2:
        y -= 1
        m += 12

    return 365 * y + y // 4 - y // 100 + y // 400 + 306 * (m + 1) // 10 + d - 429


print(f(2014, 5, 17) - f(y, m, d))
