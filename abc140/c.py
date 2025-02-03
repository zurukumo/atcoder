N = int(input())
B = [int(i) for i in input().split()]
A = [float("inf")] * N

for i in range(N - 1):
    A[i] = min(A[i], B[i])
    A[i + 1] = min(A[i + 1], B[i])

print(sum(A))
