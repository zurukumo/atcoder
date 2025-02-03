import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

p = []
m = []
zero = 0
for i in range(N):
    if A[i] > 0:
        p.append(A[i])
    elif A[i] < 0:
        m.append(-A[i])
    else:
        zero += 1

p.sort()
m.sort()

ng, ok = -(10**18) - 1, 10**18 + 1
while ok - ng > 1:
    mid = (ok + ng) // 2
    s = 0
    if mid < 0:
        j = 0
        for i in range(len(m) - 1, -1, -1):
            while j < len(p) and m[i] * p[j] < -mid:
                j += 1
            s += len(p) - j

    else:
        j = len(p) - 1
        for i in range(len(p)):
            while j >= 0 and p[i] * p[j] > mid:
                j -= 1
            s += max(0, j - i)

        j = len(m) - 1
        for i in range(len(m)):
            while j >= 0 and m[i] * m[j] > mid:
                j -= 1
            s += max(0, j - i)

        s += (len(p) + len(m)) * zero + len(p) * len(m) + zero * (zero - 1) // 2

    if s < K:
        ng = mid
    else:
        ok = mid

print(ok)
