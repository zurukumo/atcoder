import collections
import sys

sys.setrecursionlimit(10**7)

N = int(input())
S = input()

same_a2b = collections.defaultdict(int)
same_a2b = collections.defaultdict(int)
same_a2c = collections.defaultdict(int)
same_b2c = collections.defaultdict(int)
same_a2bc = collections.defaultdict(int)

ret = N * (N - 1) // 2
pa, pb, pc = 0, 0, 0
ca, cb, cc = 0, 0, 0
for ch in S:
    if ch == "A":
        ca += 1
    elif ch == "B":
        cb += 1
    else:
        cc += 1

    ret -= same_a2b[cb - ca]
    ret -= same_a2c[cc - ca]
    ret -= same_b2c[cc - cb]
    ret += same_a2bc[(cb - ca, cc - ca)] * 2

    same_a2b[pb - pa] += 1
    same_a2c[pc - pa] += 1
    same_b2c[pc - pb] += 1
    same_a2bc[(pb - pa, pc - pa)] += 1

    pa, pb, pc = ca, cb, cc


print(ret)
