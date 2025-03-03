N = int(input())
LR = [[int(i) for i in input().split()] for _ in range(N)]

max_l = -float("inf")
min_r = float("inf")
for l, r in LR:
    max_l = max(max_l, l)
    min_r = min(min_r, r)

    print(max(0, (max_l - min_r + 1) // 2))
