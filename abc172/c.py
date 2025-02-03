N, M, K = map(int, input().split())
A = [0] + [int(i) for i in input().split()]
B = [0] + [int(i) for i in input().split()]

N += 1
M += 1
for i in range(1, N) :
  A[i] += A[i - 1]
for i in range(1, M) :
  B[i] += B[i - 1]

ret = 0
a = N - 1
b = 0
while b < M :
  while a >= 0 and A[a] + B[b] > K :
    a -= 1
  if a >= 0 and A[a] + B[b] <= K :
    ret = max(ret, a + b)
  b += 1
  
print(ret)