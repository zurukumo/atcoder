import sys
input = sys.stdin.readline

H, W, M = map(int, input().split())
hw = [[int(i) for i in input().split()] for _ in range(M)]

hl = [0] * H
wl = [0] * W
mem = set()

for h, w in hw :
  hl[h - 1] += 1
  wl[w - 1] += 1
  mem.add((h - 1, w - 1))
  
mh = max(hl)
mw = max(wl)

if mh == 0 :
  print(mw)
elif mw == 0 :
  print(mh)
else :
  hs = []
  ws = []
  for i, y in enumerate(hl) :
    if y == mh :
      hs.append((i, y))
  for i, x in enumerate(wl) :
    if x == mw :
      ws.append((i, x))


  ret = 0
  for x, w in ws :
    flag = False
    for y, h in hs :
      if (y, x) in mem :
        ret = max(ret, w + h - 1)
      else :
        ret = max(ret, w + h)
        flag = True
        break
    if flag :
      break
      
  print(ret)