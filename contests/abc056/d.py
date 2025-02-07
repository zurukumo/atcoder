import sys
from bisect import bisect_left

input = sys.stdin.readline

N, K = map(int, input().split())
a = [int(i) for i in input().split()]
a.sort()
a = a[: bisect_left(a, K)]
N = len(a)


def judge(n):
    dp = [0] * K
    dp[0] = 1
    for i in range(N):
        if i == n:
            continue
        for j in range(K - a[i] - 1, -1, -1):
            if not dp[j]:
                continue
            if K - a[n] <= j + a[i]:
                return True
            dp[j + a[i]] = 1
    return False


l, r = -1, N
while r - l > 1:
    m = (l + r) // 2
    if judge(m):
        r = m
    else:
        l = m
print(r)
