N = int(input())
A = [int(i) for i in input().split()]

A.sort()
if A[0] == 1 and A[-1] == N and len(set(A)) == N:
  print('Yes')
else:
  print('No')