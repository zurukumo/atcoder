import math

A, B = map(int, input().split())

A, B = max(A, B), min(A, B)

x = math.atan2(2 * A - math.sqrt(3) * B, B)

print(min(2 * math.sqrt(3) * B / 3, B / math.cos(x)))
