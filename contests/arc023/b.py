R, C, D = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(R)]

ret = 0
for y in range(R):
    for x in range(C):
        if y + x <= D and (y + x) % 2 == D % 2:
            ret = max(ret, A[y][x])
print(ret)
