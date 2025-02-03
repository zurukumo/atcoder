import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
XC = [[int(i) for i in input().split()] for _ in range(N)]

XC.append([0, float('inf')])

XC.sort(reverse=True, key=lambda x: x[1])
dp = [0, 0]
pl, pr = 0, 0
while XC :
  x, c = XC.pop()
  l = x
  r = x
  while XC and XC[-1][1] == c :
    l = min(l, XC[-1][0])
    r = max(r, XC[-1][0])
    XC.pop()
    
  ndp = [float('inf'), float('inf')]
  ndp[0] = min(
    dp[0] + abs(pl - r) + abs(l - r),
    dp[1] + abs(pr - r) + abs(l - r) 
  )
  ndp[1] = min(
    dp[0] + abs(pl - l) + abs(l - r),
    dp[1] + abs(pr - l) + abs(l - r) 
  )
  pl, pr = l, r
  dp = ndp
  
print(min(dp))