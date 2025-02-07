N, M = map(int, input().split())
A = [int(i) for i in input().split()]

A.sort()
A = [0] + A + [N + 1]
W = []
for i in range(1, M + 2):
    a = A[i] - A[i - 1] - 1
    if a > 0:
        W.append(a)


ret = 0
if W:
    k = min(W)
    for w in W:
        ret += (w + k - 1) // k

print(ret)
