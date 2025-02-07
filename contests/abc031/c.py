N = int(input())
a = [int(i) for i in input().split()]

ret = -float("inf")
for i in range(N):
    M = -float("inf")
    Mi, Mj = None, None

    for j in range(N):
        if i == j:
            continue

        i_ = min(i, j)
        j_ = max(i, j)

        if sum(a[i_ + 1 : j_ + 1 : 2]) > M:
            M = sum(a[i_ + 1 : j_ + 1 : 2])
            Mi, Mj = i_, j_

    ret = max(ret, sum(a[Mi : Mj + 1 : 2]))

print(ret)
