import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
ABXY = [[int(i) for i in input().split()] for _ in range(T)]

for a, b, x, y in ABXY:
    x, y = abs(x), abs(y)
    ret = min(a, b) * 2 * min(x, y)
    if x > y:
        ret += min(a, 3 * b) * ((x - y + 1) // 2) + min(b, 3 * a) * ((x - y) // 2)
    elif x < y:
        ret += min(b, 3 * a) * ((y - x + 1) // 2) + min(a, 3 * b) * ((y - x) // 2)
    print(ret)
