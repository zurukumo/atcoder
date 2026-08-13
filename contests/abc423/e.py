import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
LR = [[int(i) for i in input().split()] for _ in range(Q)]

s1 = [0]
s2 = [0]
s3 = [0]

for i in range(N):
    s1.append(s1[-1] + A[i])
    s2.append(s2[-1] + A[i] * (i + 1))
    s3.append(s3[-1] + A[i] * (i + 1) * (i + 1))

for l, r in LR:
    ret = 0
    ret += -s3[r] + (l + r) * s2[r] + (-l + 1) * (r + 1) * s1[r]
    ret -= -s3[l - 1] + (l + r) * s2[l - 1] + (-l + 1) * (r + 1) * s1[l - 1]

    print(ret)
