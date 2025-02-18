H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

mod = 998244353

diff = 0
samex = 0
samey = 0
samexy = 0

if x1 == x2 and y1 == y2:
    samexy = 1
elif x1 == x2:
    samex = 1
elif y1 == y2:
    samey = 1
else:
    diff = 1


for _ in range(K):
    ndiff = diff * (H + W - 4) + samex * (H - 1) + samey * (W - 1)
    nsamex = diff + samex * (W - 2) + samexy * (W - 1)
    nsamey = diff + samey * (H - 2) + samexy * (H - 1)
    nsamexy = samex + samey

    diff = ndiff % mod
    samex = nsamex % mod
    samey = nsamey % mod
    samexy = nsamexy % mod

print(samexy)
