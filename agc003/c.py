from bisect import bisect_left

N = int(input())
A = [int(input()) for _ in range(N)]

B = sorted(A)

ret = 0
for i in range(N):
    j = bisect_left(B, A[i])
    if i % 2 != j % 2:
        ret += 1

print(ret // 2)
