N = int(input())
A = [int(i) for i in input().split()]

A.sort()

ret = 0
for i in range(N):
  ret -= A[i] * (N - i - 1)
  ret += A[i] * i
  
print(ret)