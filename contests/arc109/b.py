n = int(input())

ok = 0
ng = 10**10
while ng - ok > 1:
    mid = (ok + ng) // 2
    if mid * (mid + 1) // 2 <= n + 1:
        ok = mid
    else:
        ng = mid

print(n - ok + 1)
