from bisect import bisect_right

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort()
B.sort()
C.sort()

s = [0] * N
for i in range(N):
    s[i] = N - bisect_right(C, B[i])
for i in range(N - 2, -1, -1):
    s[i] += s[i + 1]

ret = 0
for i in range(N):
    a = bisect_right(B, A[i])
    if a < N:
        ret += s[a]
print(ret)
