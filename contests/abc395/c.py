import collections

N = int(input())
A = [int(i) for i in input().split()]

mem = collections.defaultdict(lambda: [])
for i, a in enumerate(A):
    mem[a].append(i)

ret = float("inf")
for k, v in mem.items():
    for i in range(len(v) - 1):
        ret = min(ret, v[i + 1] - v[i] + 1)

if ret == float("inf"):
    print(-1)
else:
    print(ret)
