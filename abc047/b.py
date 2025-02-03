W, H, N = map(int, input().split())

l, r, d, u = 0, W, 0, H
for _ in range(N) :
    x, y, a = map(int, input().split())
    if a == 1 :
        l = max(l, x)
    elif a == 2 :
        r = min(r, x)
    elif a == 3 :
        d = max(d, y)
    else :
        u = min(u, y)

if l <= r and d <= u :
    print((r - l) * (u - d))
else :
    print(0)