N = int(input())
A = [int(i) for i in input().split()]

ret = [0] * N
for k, v in enumerate(A):
    ret[v - 1] = k + 1

print(*ret)
