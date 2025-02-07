from collections import Counter

N, M = map(int, input().split())
A = [int(i) for i in input().split()]

for i in range(1, N):
    A[i] += A[i - 1]
for i in range(N):
    A[i] %= M

c = Counter(Counter(A + [0]).values())

ret = 0
for i, v in c.items():
    if i < 2:
        continue

    ret += v * i * (i - 1) // 2

print(ret)
