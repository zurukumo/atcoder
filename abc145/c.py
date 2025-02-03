from itertools import permutations

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for perm in permutations(range(N)):
    for i in range(1, N):
        cx, cy = xy[perm[i]]
        px, py = xy[perm[i - 1]]

        ret += pow((cx - px) ** 2 + (cy - py) ** 2, 0.5)

x = 1
for i in range(1, N + 1):
    x *= i

print(ret / x)
