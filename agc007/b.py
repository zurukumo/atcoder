N = int(input())
p = [int(i) for i in input().split()]

A = [0] * N
B = [0] * N

for i in range(1, N):
    if p[i] > p[i - 1]:
        A[p[i] - 1] = A[p[i - 1] - 1] + N * (p[i] - p[i - 1]) + 1
        B[p[i] - 1] = B[p[i - 1] - 1] - N * (p[i] - p[i - 1])
    else:
        A[p[i] - 1] = A[p[i - 1] - 1] + N * (p[i] - p[i - 1])
        B[p[i] - 1] = B[p[i - 1] - 1] - N * (p[i] - p[i - 1]) + 1

ma, mb = min(A), min(B)
for i in range(N):
    A[i] = A[i] - ma + 1
    B[i] = B[i] - mb + 1

print(*A)
print(*B)
