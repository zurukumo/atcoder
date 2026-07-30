import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()
accum = A.copy()
for i in range(N - 2, -1, -1):
    accum[i] += accum[i + 1]

ng = -1
ok = 10**10
ok_k = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    idx = bisect.bisect_left(A, mid)
    if idx < N:
        k = accum[idx] - mid * (N - idx)
    else:
        k = 0

    if k <= K:
        ok = mid
        ok_k = k
    else:
        ng = mid

ret = 0
for i in range(N):
    if A[i] > ok:
        ret += (A[i] + ok + 1) * (A[i] - (ok + 1) + 1) // 2

ret += ok * (K - ok_k)

print(ret)
