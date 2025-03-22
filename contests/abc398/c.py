import collections

N = int(input())
A = [int(i) for i in input().split()]

M = -1
cnt = collections.Counter(A)
for k, v in cnt.items():
    if v == 1:
        M = max(M, k)

if M == -1:
    print(-1)
else:
    print(A.index(M) + 1)
