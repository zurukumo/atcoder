import sys
input = sys.stdin.readline

H, W, K = map(int, input().split())
S = [[int(i) for i in input()[:-1]] for _ in range(H)]

m = float('inf')
for i in range(1 << (H - 1)) :
  pos = [0] * H
  x = 0
  for j in range(H - 1) :
    if i & (1 << j) :
      x += 1
    pos[j+1] = x
  
  ret = x
  x = 0
  cnt = [0] * H
  flag = 0
  while x < W :
    for y in range(H) :
      cnt[pos[y]] += S[y][x]
      if cnt[pos[y]] > K :
        cnt = [0] * H
        ret += 1
        flag += 1
        break
    else :
      x += 1
      flag = 0
      
    if flag == 2 :
      ret = float('inf')
      break
  
  m = min(m, ret)
  
print(m)