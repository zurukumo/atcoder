from math import sin, cos, pi

A, B = map(int, input().split())
N = int(input())
CD = [[int(i) for i in input().split()] for _ in range(N)]

if B < A:
    A, B = B, A


def check(m):
    return A * sin(m) + B * cos(m) < D + 0.01


for C, D in CD:
    if (A <= C and B <= D) or (B <= C and A <= D):
        print("YES")
        continue

    if C > D:
        C, D = D, C

    ng, ok = 0, pi / 2
    for _ in range(30):
        m = (ng + ok) / 2
        if check(m):
            ok = m
        else:
            ng = m

    if A * cos(ok) + B * sin(ok) < C + 0.01:
        print("YES")
    else:
        print("NO")
