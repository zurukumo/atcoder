N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

ret = 0
for b in B:
    ret += A[b - 1]

print(ret)
