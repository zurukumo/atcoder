xy = [[int(i) for i in input().split()] for _ in range(3)]

xs = set(x for x, y in xy)
ys = set(y for x, y in xy)

for x in xs:
    for y in ys:
        if [x, y] not in xy:
            print(x, y)
