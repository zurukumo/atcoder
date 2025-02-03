L, X, Y, S, D = map(int, input().split())

ret = float("inf")
if D >= S:
    ds = D - S
else:
    ds = D + L - S

if Y > X:
    print(min(ds / (X + Y), (L - ds) / (Y - X)))
else:
    print(ds / (X + Y))
