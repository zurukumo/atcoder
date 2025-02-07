from collections import defaultdict

N = int(input())
A = [int(i) for i in input().split()]

mod = 10**9 + 7


def prime_factor(x):
    ret = dict()
    if x % 2 == 0:
        ret[2] = 0
        while x % 2 == 0:
            x //= 2
            ret[2] += 1

    i = 3
    while i * i <= x:
        if x % i == 0:
            ret[i] = 0

            while x % i == 0:
                x //= i
                ret[i] += 1
        i += 2

    if x != 1:
        ret[x] = 1

    return ret


pr = defaultdict(int)
for i in range(N):
    for k, v in prime_factor(A[i]).items():
        pr[k] = max(pr[k], v)

a = 1
for k, v in pr.items():
    a *= pow(k, v, mod)
    a %= mod

ret = 0
for i in range(N):
    ret += a * pow(A[i], mod - 2, mod)
    ret %= mod
print(ret)
