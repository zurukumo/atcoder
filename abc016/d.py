Ax, Ay, Bx, By = map(int, input().split())
N = int(input())
XY = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N) :
  x1, y1 = XY[i]
  x2, y2 = XY[(i + 1) % N]
  
  t1 = (y1 - y2) * (Ax - x1) + (x1 - x2) * (y1 - Ay)
  t2 = (y1 - y2) * (Bx - x1) + (x1 - x2) * (y1 - By)
  t3 = (Ay - By) * (x1 - Ax) + (Ax - Bx) * (Ay - y1)
  t4 = (Ay - By) * (x2 - Ax) + (Ax - Bx) * (Ay - y2)
  
  if t1 * t2 < 0 and t3 * t4 < 0 :
    ret += 1
    
print(ret // 2 + 1)