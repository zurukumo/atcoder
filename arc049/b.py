N = int(input())
xyc = [[int(i) for i in input().split()] for _ in range(N)]

xc = []
yc = []
for x, y, c in xyc:
    xc.append((x, c))
    yc.append((y, c))


def f(tc, m):
    return max([abs(m - t) * c for t, c in tc])


ret = 0
l, r = -(10**5), 10**5
e = 1e-10
while r - l > e:
    ml = l * 2 / 3 + r / 3
    mr = l / 3 + r * 2 / 3
    if f(xc, ml) >= f(xc, mr):
        l = ml
    else:
        r = mr
ret = max(ret, f(xc, ml))

l, r = -(10**5), 10**5
while r - l > e:
    ml = l * 2 / 3 + r / 3
    mr = l / 3 + r * 2 / 3
    if f(yc, ml) >= f(yc, mr):
        l = ml
    else:
        r = mr
ret = max(ret, f(yc, ml))

print(ret)
