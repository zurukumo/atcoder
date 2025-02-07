import collections

N = int(input())
A = [int(i) for i in input().split()]

mem = collections.defaultdict(int)
s = 0
mem[0] = 1
for i, a in enumerate(A):
    if i % 2 == 0:
        s += a
    else:
        s -= a

    mem[s] += 1

ret = 0
for k, v in mem.items():
    ret += v * (v - 1) // 2
print(ret)
