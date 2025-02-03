N, K, M = map(int, input().split())
A = [int(i) for i in input().split()]

s = sum(A)
if s + K >= N * M :
  print(max(0, N * M - s))
  
else :
  print(-1)