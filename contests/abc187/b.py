N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N):
    for j in range(i + 1, N):
        xi, yi = xy[i]
        xj, yj = xy[j]

        if abs(yj - yi) <= abs(xj - xi):
            ret += 1

print(ret)
