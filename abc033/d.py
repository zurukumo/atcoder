from math import atan2, pi

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

E = 1e-10

acute = 0
right = 0

for i in range(N) :
    xs, ys = xy[i]
    arc = []
    for j in range(N) :
        if i == j :
            continue
        xt, yt = xy[j]
        arc.append(atan2(yt-ys, xt-xs))
    
    arc.sort()
    for j in range(N-1) :
        arc.append(arc[j]+pi*2)
    to = 0
    for fr in range(N-1) :
        while 2*(arc[to+1] - arc[fr] + E) < pi :
            to += 1
        if abs(2*(arc[to+1] - arc[fr]) - pi) < E :
            right += 1
        acute += to - fr
        if fr == to :
            to += 1
                
obtuse = N*(N-1)*(N-2)//2-acute-right
print(N*(N-1)*(N-2)//6-right-obtuse, right, obtuse)