A, B, C, X, Y = map(int, input().split())

ret = float("inf")
for ab in range(0, max(X, Y) * 2 + 1, 2):
    ret = min(ret, A * max(0, (X - ab // 2)) + B * max(0, (Y - ab // 2)) + C * ab)

print(ret)
