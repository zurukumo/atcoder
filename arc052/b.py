import math

N, Q = map(int, input().split())
XRH = [[int(i) for i in input().split()] for _ in range(N)]
AB = [[int(i) for i in input().split()] for _ in range(Q)]

XRHV = []
for X, R, H in XRH:
    XRHV.append((X, R, H, R * R * math.pi * H / 3))

dp = [0] * 20001
for i in range(1, 20001):
    s = 0
    for X, R, H, V in XRHV:
        if X <= i:
            if i < X + H:
                s += V * (1 - ((X + H - i) ** 3) / (H**3))
            else:
                s += V
    dp[i] = s

for A, B in AB:
    print(dp[B] - dp[A])
