from math import sqrt

txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if sqrt((x - txa) ** 2 + (y - tya) ** 2) + sqrt((x - txb) ** 2 + (y - tyb) ** 2) <= T * V:
        print("YES")
        break
else:
    print("NO")
