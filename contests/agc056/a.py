N = int(input())

ret = [["."] * N for _ in range(N)]


for y in range(N - N % 3):
    for x in range(y // 3, N - N % 3, N // 3):
        ret[y][x] = "#"

if N % 3 == 1:
    for y in range(N - 4, N):
        for x in range(N - 3, N):
            ret[y][x] = "."

    ret[-1][-1] = "#"
    ret[-1][-2] = "#"
    ret[-1][-3] = "#"
    ret[-2][-2] = "#"
    ret[-3][-2] = "#"
    ret[-4][-1] = "#"
    ret[-5][-1] = "#"
    ret[-5][-3] = "."


elif N % 3 == 2:
    for y in range(N - 5, N):
        for x in range(N - 3, N):
            ret[y][x] = "."

    ret[-1][-1] = "#"
    ret[-1][-2] = "#"
    ret[-1][-3] = "#"
    ret[-2][-1] = "#"
    ret[-2][-2] = "#"
    ret[-2][-3] = "#"
    ret[-3][-3] = "#"
    ret[-4][-2] = "#"
    ret[-5][-1] = "#"

for row in ret:
    print("".join(row))
