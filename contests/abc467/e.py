import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

es = []
os = []
sumb = 0
for i in range(N - 1):
    sumb = B[i] - sumb
    if i % 2 == 0:
        es.append((sumb - A[0] - A[i + 1]) % M + 1)
    else:
        x = -(sumb + A[0] - A[i + 1]) % M
        if x != 0:
            os.append(x)

es.sort()
os.sort()


s = 0
for i in range(N - 1):
    diff = (B[i] - A[i] - A[i + 1]) % M
    s += diff
    A[i + 1] += diff
    A[i + 1] %= M


ret = s
for i, o in enumerate(os):
    j = bisect.bisect_left(es, o + 1) - 1
    if len(es) == len(os):
        ret = min(ret, s - M * (i - j) + o)
    else:
        ret = min(ret, s - M * (i - j))

print(ret)
