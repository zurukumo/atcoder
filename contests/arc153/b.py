H, W = map(int, input().split())
A = [input() for _ in range(H)]
Q = int(input())
ab = [[int(i) for i in input().split()] for _ in range(Q)]

x_head = 0
y_head = 0
rev = False
for a, b in ab:
    if rev:
        x_head -= b - 1
    else:
        x_head += b - 1
    x_head %= W

    if rev:
        y_head -= a - 1
    else:
        y_head += a - 1
    y_head %= H

    rev = not rev

xs = []
ys = []

i = x_head
j = y_head
for _ in range(W):
    xs.append(i)
    if rev:
        i -= 1
    else:
        i += 1
    i %= W
for _ in range(H):
    ys.append(j)
    if rev:
        j -= 1
    else:
        j += 1
    j %= H


for i in range(H):
    print("".join(A[ys[i]][xs[j]] for j in range(W)))
