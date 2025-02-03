from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

q = []
for y in range(H) :
    for x in range(W) :
        if A[y][x] == '#' :
            q.append((y, x))

ret = 0
while True :
    r = []
    while q :
        cy, cx = q.pop()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)) :
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < H and 0 <= nx < W and A[ny][nx] == '.' :
                A[ny][nx] = '#'
                r.append((ny, nx))
    ret += 1
    if len(r) == 0 :
        break
    
    q = r
    
print(ret - 1)