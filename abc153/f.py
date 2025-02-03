import sys
input = sys.stdin.readline

from heapq import heappush, heappop

N, D, A = map(int, input().split())
XH = [[int(i) for i in input().split()] for _ in range(N)]

XH.sort()

ret = 0
hp = []
s = 0
for i, (x, h) in enumerate(XH) :
  while len(hp) > 0 and hp[0][0] < x - D :
    s -= heappop(hp)[1]
    
  if s > h :
    continue
  
  cnt = (h - s + A - 1) // A
  ret += cnt
  heappush(hp, (x + D, cnt * A))
  s += cnt * A

print(ret)