N, M = map(int, input().split())
sc = [[int(i) for i in input().split()] for _ in range(M)]

if N == 1 :
  start = 0
else :
  start = 10 ** (N - 1)
  
ret = float('inf')
for i in range(start, 10 ** N) :
  i = str(i)
  for s, c in sc :
    if int(i[s - 1]) != c :
      break
  else :
    ret = min(ret, int(i))
    
if ret == float('inf') :
  print(-1)
else :
  print(ret)