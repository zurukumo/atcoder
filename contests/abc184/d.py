from collections import defaultdict

A, B, C = map(int, input().split())

ret = 0
dp = defaultdict(int)
dp[(A, B, C)] = 1
for i in range(1, 300):
    ndp = defaultdict(int)
    for (x, y, z), v in dp.items():
        if x == 100 or y == 100 or z == 100:
            ret += (i - 1) * v
            continue
        if x > 0:
            ndp[(x + 1, y, z)] += v * x / (x + y + z)
        if y > 0:
            ndp[(x, y + 1, z)] += v * y / (x + y + z)
        if z > 0:
            ndp[(x, y, z + 1)] += v * z / (x + y + z)
    dp = ndp

print(ret)
