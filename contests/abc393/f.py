import bisect

N, Q = map(int, input().split())
A = [int(i) for i in input().split()]
RX = [[int(i) for i in input().split()] for _ in range(Q)]

RXi = [(r, x, i) for i, (r, x) in enumerate(RX)]
RXi.sort(key=lambda rxi: rxi[0])

j = 0
lis = [A[0]]
ret = [0] * Q
for r, x, i in RXi:
    while j < r:
        new = A[j]
        if new > lis[-1]:
            lis.append(new)
        else:
            lis[bisect.bisect_left(lis, new)] = new
        j += 1
    ret[i] = bisect.bisect_left(lis, x + 1)

for r in ret:
    print(r)
