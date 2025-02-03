N, L = map(int, input().split())
xd = [input().split() for _ in range(N)]

for i in range(N):
    xd[i][0] = int(xd[i][0])

if xd[0][1] == "L":
    xd = [[0, "R"]] + xd
if xd[-1][1] == "R":
    xd = xd + [[L + 1, "L"]]
N = len(xd)

ret = 0
for i in range(N - 1):
    if xd[i][1] == "R" and xd[i + 1][1] == "L":
        cr, cl = 1, 1
        for j in range(i - 1, -1, -1):
            if xd[j][1] == "L":
                break
            ret += xd[i][0] - xd[j][0] - cr
            cr += 1
        for j in range(i + 2, N):
            if xd[j][1] == "R":
                break
            ret += xd[j][0] - xd[i + 1][0] - cl
            cl += 1
        ret += max(cl, cr) * (xd[i + 1][0] - xd[i][0] - 1)

print(ret)
