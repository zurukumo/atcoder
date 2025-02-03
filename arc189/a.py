N = int(input())
A = [int(i) for i in input().split()]


def solve(N, A):
    mod = 998244353

    fac = [0] * (N + 1)
    inv = [0] * (N + 1)

    fac[0] = 1
    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i
        fac[i] %= mod
    inv[N] = pow(fac[N], mod - 2, mod)
    for i in range(N, 0, -1):
        inv[i - 1] = inv[i] * i
        inv[i - 1] %= mod

    fac2 = [0] * N
    fac2[1] = 1
    for i in range(3, N, 2):
        fac2[i] = fac2[i - 2] * i
        fac2[i] %= mod

    ret = 1
    pre = A[0]
    cnt = 1
    for i, a in enumerate(A[1:] + [2]):
        if a == pre:
            cnt += 1
        else:
            if cnt % 2 == 0:
                return 0
            if pre == (i % 2):
                return 0

            if cnt >= 3:
                ret *= fac2[cnt - 2]
                ret %= mod
                ret *= inv[cnt // 2]
                ret %= mod
            cnt = 1
            pre = a

    s = 0
    for i, a in enumerate(A):
        if i % 2 == a:
            s += 1

    ret *= fac[s]
    ret %= mod

    return ret


print(solve(N, A))
