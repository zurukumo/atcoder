N = int(input())
A = [int(i) for i in input().split()]

ret = float('inf')
for i in range(1 << N):
  tmp = 0
  s = 0
  for j in range(N):
    s |= A[j]
    if i & (1 << j):
      tmp ^= s
      s = 0
  else :
    if s > 0 :
      tmp ^= s
    ret = min(ret, tmp)
    
print(ret)