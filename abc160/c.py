K, N = map(int, input().split())
A = [int(i) for i in input().split()]

M = K - (A[-1] - A[0])
for i in range(1, N) :
  M = max(M, A[i] - A[i-1])

print(K - M)