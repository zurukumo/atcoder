N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ret = 0
for i in range(N):
    if B[i] > A[i]:
        B[i] -= A[i]
        ret += A[i]
        A[i] = 0

    else:
        A[i] -= B[i]
        ret += B[i]
        B[i] = 0

    if B[i] > A[i + 1]:
        B[i] -= A[i + 1]
        ret += A[i + 1]
        A[i + 1] = 0

    else:
        A[i + 1] -= B[i]
        ret += B[i]
        B[i] = 0

print(ret)
