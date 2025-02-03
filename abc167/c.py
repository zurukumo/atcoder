import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
CA = [[int(i) for i in input().split()] for _ in range(N)]

ret = float('inf')
for mask in range(1 << N) :
  tot = [0] * (M + 1)
  for i in range(N) :
    if mask & (1 << i) :
      for j in range(M + 1) :
        tot[j] += CA[i][j]
        
  if min(tot[1:]) >= X :
    ret = min(ret, tot[0])
    
if ret == float('inf') :
  print(-1)
else :
  print(ret)