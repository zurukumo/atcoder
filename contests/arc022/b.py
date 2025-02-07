N = int(input())
A = [int(i) for i in input().split()]


def check(m):
    taste = [0] * (10**5 + 1)
    over2 = 0
    for i in range(m):
        taste[A[i]] += 1
        if taste[A[i]] == 2:
            over2 += 1

    if over2 == 0:
        return True

    for i in range(m, N):
        taste[A[i - m]] -= 1
        if taste[A[i - m]] == 1:
            over2 -= 1
        taste[A[i]] += 1
        if taste[A[i]] == 2:
            over2 += 1

        if over2 == 0:
            return True

    return False


ok, ng = 1, N + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid

print(ok)
