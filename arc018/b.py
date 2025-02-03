N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for a in range(N) :
    for b in range(a + 1, N) :
        for c in range(b + 1, N) :
            ax, ay = xy[a]
            bx, by = xy[b]
            cx, cy = xy[c]
            bx, by = bx - ax, by - ay
            cx, cy = cx - ax, cy - ay
            S = bx * cy - by * cx
            if S != 0 and S % 2 == 0 :
                ret += 1
                
print(ret)