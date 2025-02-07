N = int(input())
A = [int(i) for i in input().split()]

ret = 0
for a in A:
    ret += a * a * (N - 1)

B = A[::-1]
for i in range(1, N):
    B[i] += B[i - 1]
B = B[::-1]

for i in range(N - 1):
    ret -= 2 * A[i] * B[i + 1]

print(ret)
