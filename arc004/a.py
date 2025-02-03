N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N):
    xi, yi = xy[i]
    for j in range(i + 1, N):
        xj, yj = xy[j]
        ret = max(ret, ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5)

print(ret)
