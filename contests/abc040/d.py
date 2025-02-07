import sys

input = sys.stdin.readline

schedule1 = []
schedule2 = []

N, M = map(int, input().split())
for _ in range(M):
    a, b, y = map(int, input().split())
    schedule2.append((-y, 1, a - 1, b - 1))
Q = int(input())
for i in range(Q):
    v, w = map(int, input().split())
    schedule1.append((-w, 0, v - 1, i))

schedule = schedule1 + schedule2
schedule.sort()

par = [-1] * N
s = [1] * N


def root(x):
    while par[x] >= 0:
        x = par[x]
    return x


def unite(x, y):
    rx = root(x)
    ry = root(y)

    if rx != ry:
        if par[rx] > par[ry]:
            par[rx] = ry
        else:
            if par[rx] == par[ry]:
                par[rx] -= 1
            par[ry] = rx

        S = s[rx] + s[ry]
        s[rx] = s[ry] = S

    return


ret = [0] * Q
for sch in schedule:
    if sch[1]:
        unite(sch[2], sch[3])
    else:
        ret[sch[3]] = s[root(sch[2])]

for i in range(Q):
    print(ret[i])
