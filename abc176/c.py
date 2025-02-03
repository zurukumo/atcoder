N = int(input())
A = [int(i) for i in input().split()]

ret = 0
for i in range(1, N) :
  if A[i] < A[i - 1] :
    ret += A[i - 1] - A[i]
    A[i] = A[i - 1]

print(ret)