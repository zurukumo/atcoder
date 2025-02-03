import sys
sys.setrecursionlimit(10**5)

H, W, D = map(int, input().split())
A = [[int(i) - 1 for i in input().split()] for _ in range(H)]
Q = int(input())
LR = [[int(i) for i in input().split()] for _ in range(Q)]

place = [0] * (H * W)
for i in range(H) :
    for j in range(W) :
        place[A[i][j]] = (i, j)

cost = [0] * (H * W)
def dfs(i, px, py) :
    if i + D >= H * W :
        return 0
        
    cx, cy = place[i + D]
    cost[i] = dfs(i + D, cx, cy) + abs(cx - px) + abs(cy - py)
    return cost[i]
    
for i in range(D) :
    dfs(i, place[i][0], place[i][1])
    
for l, r in LR :
    print(cost[l-1] - cost[r-1])