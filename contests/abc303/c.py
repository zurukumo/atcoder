N, M, H, K = map(int, input().split())
S = input()
xy = [[int(i) for i in input().split()] for _ in range(M)]

portions = set()
for x, y in xy:
    portions.add((y, x))

cy, cx = 0, 0
for s in S:
    H -= 1
    if H < 0:
        print("No")
        exit()
    if s == "U":
        cy += 1
    elif s == "D":
        cy -= 1
    elif s == "L":
        cx -= 1
    elif s == "R":
        cx += 1
    if (cy, cx) in portions and H < K:
        H = K
        portions.remove((cy, cx))

print("Yes")
