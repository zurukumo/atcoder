H, W = map(int, input().split())
A = [[i for i in input()] for _ in range(H)]

cnt = 0
for y in range(H):
    cnt += A[y].count("#")

y, x = 0, 0
cnt -= 1
while not (y == H - 1 and x == W - 1):
    if x + 1 < W and A[y][x + 1] == "#":
        cnt -= 1
        x += 1
        continue

    if y + 1 < H and A[y + 1][x] == "#":
        cnt -= 1
        y += 1
        continue

    break

if cnt == 0:
    print("Possible")
else:
    print("Impossible")
