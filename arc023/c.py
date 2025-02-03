N = int(input())
A = [int(i) for i in input().split()]

mod = 10**9 + 7


def comb(n, r):
    if r == 0 or n < r:
        return 1
    ret = 1
    for i in range(r):
        ret *= n - i
        ret *= pow(i + 1, mod - 2, mod)
        ret %= mod
    return ret


ret = 1
l = 1
emp = 0
for i in range(N):
    if A[i] == -1:
        emp += 1
    else:
        ret *= comb(A[i] - l + emp, emp)
        ret %= mod
        l = A[i]
        emp = 0

print(ret)
