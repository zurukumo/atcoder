N = int(input())
T = input()

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
di = 0

x, y = 0, 0
for t in T:
    if t == "S":
        x += d[di][0]
        y += d[di][1]
    elif t == "R":
        di = (di + 1) % 4

print(x, y)
