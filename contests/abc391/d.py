N, W = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
TA = [[int(i) for i in input().split()] for _ in range(Q)]

xyi = [(i, x - 1, y - 1) for i, (x, y) in enumerate(XY)]
xyi.sort(key=lambda x: x[2], reverse=True)

y_by_x = [[] for _ in range(W)]
for i, x, y in xyi:
    y_by_x[x].append((i, y))

when = [-1] * N


def create_when():
    while True:
        ret = 0
        for i in range(W):
            if not y_by_x[i]:
                return
            ret = max(ret, y_by_x[i][-1][1])

        for i in range(W):
            when[y_by_x[i].pop()[0]] = ret + 1


create_when()


for t, a in TA:
    if when[a - 1] == -1 or t < when[a - 1]:
        print("Yes")
    else:
        print("No")
