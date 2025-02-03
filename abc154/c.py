N = int(input())
A = [int(i) for i in input().split()]

if len(A) == len(set(A)) :
  print('YES')
else :
  print('NO')