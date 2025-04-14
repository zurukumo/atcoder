N = int(input())


def f(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


ret = float("inf")
a = 0
b = 10**6
while a <= 10**6:
    while b >= 0 and f(a, b) >= N:
        ret = min(ret, f(a, b))
        b -= 1
    a += 1

print(ret)
