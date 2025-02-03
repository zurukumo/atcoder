from collections import defaultdict

N, M = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(M)]

ys = defaultdict(lambda: [])
for X, Y in XY:
    ys[X].append(Y)
keys = list(ys.keys())
keys.sort()

cur = set([N])
for key in keys:
    a = []
    r = []
    # print(ys[key], cur)
    for x in ys[key]:
        if x in cur:
            r.append(x)
        if x + 1 in cur or x - 1 in cur:
            a.append(x)

    # print(a)
    # print(r)
    for rr in r:
        if rr in cur:
            cur.remove(rr)
    for aa in a:
        if aa not in cur:
            cur.add(aa)
    # print()

print(len(cur))
