N, M, C = map(int, input().split())
B = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N):
    s = C
    for j in range(M):
        s += A[i][j] * B[j]
    if s > 0:
        ret += 1
print(ret)
