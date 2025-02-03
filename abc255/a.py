R, C = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(2)]

print(A[R - 1][C - 1])
