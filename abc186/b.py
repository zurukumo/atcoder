H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]

s = 0
m = float("inf")
for y in range(H):
    for x in range(W):
        s += A[y][x]
        m = min(m, A[y][x])

print(s - m * H * W)
