N = int(input())


def root(x):
    ok = 0
    ng = 10**10
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if mid * mid <= x:
            ok = mid
        else:
            ng = mid
    return ok


ret = root(N // 4) + root(N // 2)

print(ret)
