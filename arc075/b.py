import sys

input = sys.stdin.readline

N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]


def judge(m):
    s = 0
    for i in range(N):
        t = max(0, (h[i] - m * B + A - B - 1) // (A - B))
        s += t
        if s > m:
            return False
    return True


h.sort(reverse=True)
l, r = -1, 10**9 + 1
while r - l > 1:
    m = (l + r) // 2
    if judge(m):
        r = m
    else:
        l = m

print(r)
