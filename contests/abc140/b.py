N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

ret = 0
pre = -3
for i in range(N):
    ret += B[A[i] - 1]
    if A[i] - 1 == pre + 1:
        ret += C[pre]
    pre = A[i] - 1

print(ret)
