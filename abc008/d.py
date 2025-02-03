W, H = map(int, input().split())
N = int(input())
XY = [[int(i) for i in input().split()] for _ in range(N)]

dp = dict()

def f(xa, ya, xb, yb) :
  if (xa, ya, xb, yb) in dp :
    return dp[(xa, ya, xb, yb)]
   
  ret = 0
  for i in range(N) :
    x, y = XY[i]
    if xa <= x <= xb and ya <= y <= yb :
      tmp = xb - xa + yb - ya + 1
      tmp += f(xa, ya, x - 1, y - 1)
      tmp += f(x + 1, ya, xb, y - 1)
      tmp += f(xa, y + 1, x - 1, yb)
      tmp += f(x + 1, y + 1, xb, yb)
      ret = max(ret, tmp)
      
  dp[(xa, ya, xb, yb)] = ret
  return ret
  
print(f(1, 1, W, H))