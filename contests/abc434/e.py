import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
XR = [[int(i) for i in input().split()] for _ in range(N)]

counter = collections.defaultdict(set)
for i, (x, r) in enumerate(XR):
    counter[x - r].add(i)
    counter[x + r].add(i)

queue = []
for k, v in counter.items():
    if len(v) == 1:
        queue.append(k)

ret = 0
while queue:
    k = queue.pop()
    if len(counter[k]) == 0:
        continue
    i = list(counter[k])[0]
    x, r = XR[i]
    if x - r == k and i in counter[x + r]:
        counter[x + r].remove(i)
        ret += 1
        if len(counter[x + r]) == 1:
            queue.append(x + r)
    elif x + r == k and i in counter[x - r]:
        counter[x - r].remove(i)
        ret += 1
        if len(counter[x - r]) == 1:
            queue.append(x - r)

for k, v in counter.items():
    if len(v) > 1:
        ret += 1


print(ret)
