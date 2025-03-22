N, R, C = map(int, input().split())
S = input()

ret = ""
x, y = 0, 0
done = set([(0, 0)])
for i, c in enumerate(S):
    if c == "N":
        y -= 1
    elif c == "S":
        y += 1
    elif c == "E":
        x += 1
    else:
        x -= 1

    if ((x - C), (y - R)) in done:
        ret += "1"
    else:
        ret += "0"

    done.add((x, y))

print(ret)
