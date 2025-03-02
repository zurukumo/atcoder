N, Q = map(int, input().split())
PV = [[int(i) for i in input().split()] for _ in range(Q)]

mod = 998244353

for i, (pi, vi) in enumerate(PV):
    l = r = False
    # 自分より前に自分より大きいやつがいるか
    for pj, vj in PV[:i]:
        if pj <= pi and vj > vi:
            l |= True
        if pj >= pi and vj > vi:
            r |= True
    # 自分より後に自分より小さいやつがいるか
    for pj, vj in PV[i + 1 :]:
        if pj <= pi and vj < vi:
            l |= True
        if pj >= pi and vj < vi:
            r |= True

    if l and r:
        print(0)
        exit()

cnt = 0
for i in range(Q):
    lmax = -float("inf")
    rmin = float("inf")
    for j in range(i):
        lmax = max(lmax, PV[j][1])
    for j in range(i + 1, Q):
        rmin = min(rmin, PV[j][1])
    if lmax <= PV[i][1] <= rmin:
        cnt += 1

print(pow(2, cnt, mod))
