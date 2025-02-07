N = int(input())
A = [int(i) for i in input().split()]
B = [A[0]]
for i in range(1, N):
    if A[i] != B[-1]:
        B.append(A[i])

N = len(B)

ret = 1
i = 2
while i < N:
    if (B[i] - B[i - 1]) * (B[i - 1] - B[i - 2]) < 0:
        ret += 1
        i += 1
    i += 1

print(ret)
