import collections

N = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

acounter = collections.Counter(a)
bcounter = collections.Counter(b)

counter = collections.defaultdict(int)
for ak, av in acounter.items():
    for bk, bv in bcounter.items():
        counter[ak ^ bk] += min(av, bv)

ret = []
for k, v in counter.items():
    if v == N:
        ret.append(k)

ret.sort()
print(len(ret))
for r in ret:
    print(r)
