xy = [[int(i) for i in input().split()] for _ in range(3)]

a2 = (xy[0][0] - xy[1][0]) ** 2 + (xy[0][1] - xy[1][1]) ** 2
b2 = (xy[1][0] - xy[2][0]) ** 2 + (xy[1][1] - xy[2][1]) ** 2
c2 = (xy[2][0] - xy[0][0]) ** 2 + (xy[2][1] - xy[0][1]) ** 2

a2, b2, c2 = sorted([a2, b2, c2])
if a2 + b2 == c2:
    print('Yes')
else:
    print('No')
