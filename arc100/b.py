from bisect import bisect_left

N = int(input())
A = [int(i) for i in input().split()]

s = sum(A)
for i in range(1, N):
    A[i] += A[i - 1]

ret = float("inf")
for b in range(1, N - 1):
    a = bisect_left(A, A[b] / 2)
    c = bisect_left(A, A[b] + (s - A[b]) / 2)
    for i in [a - 1, a]:
        for j in [c - 1, c]:
            if not 0 <= i < b < j < N - 1:
                continue
            cut = [A[i], A[b] - A[i], A[j] - A[b], s - A[j]]
            ret = min(ret, max(cut) - min(cut))

print(ret)
