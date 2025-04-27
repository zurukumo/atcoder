import collections

N, D = map(int, input().split())
A = [int(i) for i in input().split()]


if D == 0:
    print(N - len(set(A)))
    exit()

ret = 0
counter = collections.Counter(A)
visited = set()

for i in sorted(counter.keys()):
    if i in visited:
        continue

    now = i
    a, b = 10**15, 0
    while now in counter:
        visited.add(now)
        a, b = b, min(a, b) + counter[now]
        now += D

    ret += min(a, b)

print(ret)
