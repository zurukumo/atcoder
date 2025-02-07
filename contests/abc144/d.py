import math

a, b, x = map(int, input().split())

t = 2 * x / (a * a) - b
if t >= 0:
    print(math.degrees(math.atan2(2 * b - 2 * x / (a * a), a)))
else:
    print(math.degrees(math.atan2(b, 2 * x / (a * b))))
