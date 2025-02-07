from collections import defaultdict

N = int(input())
A = [0] + [int(i) for i in input().split()]

cnt = defaultdict(int)
cnt[0] += 1

ret = 0
for i in range(1, N + 1):
    A[i] += A[i - 1]
    ret += cnt[A[i]]
    cnt[A[i]] += 1

print(ret)
