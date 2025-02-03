N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

A, B = map(list, zip(*AB))
A.sort()
B.sort()

if N % 2 == 0 :
  print(B[N//2] + B[N//2-1] - A[N//2] - A[N//2-1] + 1)
else :
  print(B[N//2] - A[N//2] + 1)