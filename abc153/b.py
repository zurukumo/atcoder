H, N = map(int, input().split())
A = [int(i) for i in input().split()]

if sum(A) >= H :
  print('Yes')
else :
  print('No')