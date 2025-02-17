N = int(input())
A = [int(i) for i in input().split()]

ret = 0
for i in range(1, 2 * N - 1):
    if A[i - 1] == A[i + 1]:
        ret += 1
print(ret)
