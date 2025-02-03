from heapq import heappush, heappop
from math import sqrt

xs, ys, xt, yt = map(int, input().split())
N = int(input())
xyr = [[int(i) for i in input().split()] for _ in range(N)]

cost = [0] * N
h = []

def dist(x, y) :
    return sqrt(x ** 2 + y ** 2)

for i, (x, y, r) in enumerate(xyr) :
    d = max(0, dist(xs-x, ys-y) - r)
    heappush(h, (d, i))
    cost[i] = d
 
while h :
    dc, i = heappop(h)
    if cost[i] < dc :
        continue
        
    xc, yc, rc = xyr[i]
    
    for i, (x, y, r) in enumerate(xyr) :
        d = dc + max(0, dist(xc-x, yc-y) - rc - r)
        if d < cost[i] :
            heappush(h, (d, i))
            cost[i] = d
            
ret = sqrt((xs-xt) ** 2 + (ys-yt)**2)
for i, (x, y, r) in enumerate(xyr) :
    ret = min(ret, cost[i] + max(0, dist(xt-x, yt-y) - r))
    
print(ret)