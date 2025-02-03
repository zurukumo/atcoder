import sys

input = sys.stdin.readline
from bisect import bisect_left, bisect_right

H, W, N, M = map(int, input().split())
AB = [[int(i) - 1 for i in input().split()] for _ in range(N)]
CD = [[int(i) - 1 for i in input().split()] for _ in range(M)]

CD.sort(key=lambda x: x[1])
Xpos = [[-1] for _ in range(H)]
for C, D in CD:
    Xpos[C].append(D)
for i in range(H):
    Xpos[i].append(W)

CD.sort(key=lambda x: x[0])
Ypos = [[-1] for _ in range(W)]
for C, D in CD:
    Ypos[D].append(C)
for i in range(W):
    Ypos[i].append(H)

Xfield = [[0] * (W + 1) for _ in range(H)]
Yfield = [[0] * (H + 1) for _ in range(W)]
for A, B in AB:
    f = Xpos[A][bisect_left(Xpos[A], B) - 1] + 1
    t = Xpos[A][bisect_right(Xpos[A], B)]
    Xfield[A][f] += 1
    Xfield[A][t] -= 1

for A, B in AB:
    f = Ypos[B][bisect_left(Ypos[B], A) - 1] + 1
    t = Ypos[B][bisect_right(Ypos[B], A)]
    Yfield[B][f] += 1
    Yfield[B][t] -= 1

for i in range(H):
    for j in range(1, W + 1):
        Xfield[i][j] += Xfield[i][j - 1]

for i in range(W):
    for j in range(1, H + 1):
        Yfield[i][j] += Yfield[i][j - 1]

ret = 0
for i in range(H):
    for j in range(W):
        if Xfield[i][j] or Yfield[j][i]:
            ret += 1

print(ret)
