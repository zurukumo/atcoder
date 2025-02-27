N = int(input())
W = [int(i) for i in input().split()]
LR = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
st = [[int(i) for i in input().split()] for _ in range(Q)]


lmin = [float("inf")] * (2 * N + 2)
rmin = [float("inf")] * (2 * N + 2)
for i, (l, r) in enumerate(LR):
    lmin[r + 1] = min(lmin[r + 1], W[i])
    rmin[l - 1] = min(rmin[l - 1], W[i])


for i in range(1, 2 * N + 2):
    lmin[i] = min(lmin[i], lmin[i - 1])
for i in range(2 * N, -1, -1):
    rmin[i] = min(rmin[i], rmin[i + 1])

for s, t in st:
    s -= 1
    t -= 1
    l1, r1 = LR[s]
    l2, r2 = LR[t]
    if r1 < l2 or r2 < l1:
        print(W[s] + W[t])
    else:
        mid = min(
            lmin[min(l1, l2)],
            rmin[max(r1, r2)],
            lmin[l1] + lmin[l2],
            lmin[l1] + rmin[r2],
            lmin[l2] + rmin[r1],
            rmin[r1] + rmin[r2],
        )
        if mid == float("inf"):
            print(-1)
        else:
            print(W[s] + W[t] + mid)
