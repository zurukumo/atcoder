import bisect

N = int(input())
ac = [input().split() for _ in range(2 * N)]

r = []
g = []
b = []

for a, c in ac:
    a = int(a)
    match c:
        case "R":
            r.append(a)
        case "G":
            g.append(a)
        case "B":
            b.append(a)

r.sort()
g.sort()
b.sort()

if len(r) % 2 == 0 and len(g) % 2 == 0 and len(b) % 2 == 0:
    print(0)
    exit()

if len(r) % 2 == 0:
    e, o1, o2 = r, g, b
elif len(g) % 2 == 0:
    e, o1, o2 = g, r, b
else:
    e, o1, o2 = b, r, g

ret = float("inf")

# 奇数グループと奇数グループを同室にするパターン
for c in o1:
    l = bisect.bisect_right(o2, c)
    if 0 <= l - 1:
        ret = min(ret, abs(c - o2[l - 1]))
    r = bisect.bisect_left(o2, c)
    if r < len(o2):
        ret = min(ret, abs(c - o2[r]))

# 奇数グループと偶数グループを同室にするのを2回繰り返すパターン
m1 = float("inf")
m2 = float("inf")
for c in o1:
    l = bisect.bisect_right(e, c)
    if 0 <= l - 1:
        m1 = min(m1, abs(c - e[l - 1]))
    r = bisect.bisect_left(e, c)
    if r < len(e):
        m1 = min(m1, abs(c - e[r]))
for c in o2:
    l = bisect.bisect_right(e, c)
    if 0 <= l - 1:
        m2 = min(m2, abs(c - e[l - 1]))
    r = bisect.bisect_left(e, c)
    if r < len(e):
        m2 = min(m2, abs(c - e[r]))
ret = min(ret, m1 + m2)

print(ret)
