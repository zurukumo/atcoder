X = [int(i) for i in input()]
M = int(input())

if len(X) == 1:
    if X[0] <= M:
        print(1)
    else:
        print(0)
else:
    d = int(sorted(X)[-1])
    ok = d
    ng = M + 100
    X = X[::-1]
    while ng - ok > 1:
        m = (ok + ng) // 2
        ret = 0
        for i, x in enumerate(X):
            ret += pow(m, i) * x
        if ret <= M:
            ok = m
        else:
            ng = m

    print(ok - d)
