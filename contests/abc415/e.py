import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
P = [int(i) for i in input().split()]


def judge(mid):
    if mid + A[0][0] < P[0]:
        return False
    ma = [[-float("inf")] * (W + 1) for _ in range(H + 1)]
    ma[0][-1] = ma[-1][0] = mid

    for k in range(H + W - 1):
        for y in range(max(0, k - W + 1), min(k + 1, H)):
            x = k - y
            nc = max(ma[y - 1][x] + A[y][x] - P[y + x], ma[y][x - 1] + A[y][x] - P[y + x])
            if nc >= 0:
                ma[y][x] = nc

    return ma[H - 1][W - 1] >= 0


ng = -1
ok = 10**15
while ok - ng > 1:
    mid = (ok + ng) // 2
    if judge(mid):
        ok = mid
    else:
        ng = mid

print(ok)
