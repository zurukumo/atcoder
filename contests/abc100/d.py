N, M = map(int, input().split())
xyz = [[int(i) for i in input().split()] for _ in range(N)]

ret = -float("inf")
for i in [-1, 1]:
    for j in [-1, 1]:
        for k in [-1, 1]:
            ret = max(ret, sum(sorted([x * i + y * j + z * k for x, y, z in xyz])[N - M :]))

print(ret)
