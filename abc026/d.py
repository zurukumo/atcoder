import math

A, B, C = map(int, input().split())


def f(x):
    return A * x + B * math.sin(C * x * math.pi) - 100


left = (100 - B) / A
right = (100 + B) / A

while True:
    mid = (left + right) / 2

    if abs(f(mid)) <= 10**-6:
        break

    if f(mid) <= 0:
        left = mid
    else:
        right = mid

print(mid)
