x, y = map(int, input().split())

if x > y:
    x, y = y, x

if x == y:
    print(x)
elif 0 not in [x, y]:
    print(0)
elif 1 not in [x, y]:
    print(1)
elif 2 not in [x, y]:
    print(2)
