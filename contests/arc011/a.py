m, n, N = map(int, input().split())

ret = 0
old, new = 0, N
while True:
    ret += new
    old += new
    new = old // m * n
    old = old % m
    if new == 0:
        break
ret += new

print(ret)
