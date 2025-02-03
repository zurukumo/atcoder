from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]

mem = defaultdict(int)
for i in range(N):
    mem[A[i]] += 1

ret = 0
for v in mem.values():
    if v % 2 == 1:
        ret += 1
print(ret)
