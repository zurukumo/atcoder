N, X = map(int, input().split())
A = [int(i) for i in input().split()]

ret = 0
for i, a in enumerate(A):
  if i % 2 == 1:
    ret += a - 1
  else:
    ret += a
    
if ret <= X:
  print('Yes')
else:
  print('No')