import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T, M = map(int, input().split())

primes = [2]
for i in range(3, 5000 + 1, 2):
    flag = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            flag = False
            break
    if flag:
        primes.append(i)

fact_prime_factors = [collections.defaultdict(int), collections.defaultdict(int)]
for i in range(2, 5000 + 1):
    pfs = fact_prime_factors[-1].copy()
    for p in primes:
        if p * p > i:
            break
        while i % p == 0:
            pfs[p] += 1
            i //= p

    if i != 1:
        pfs[i] += 1

    fact_prime_factors.append(pfs)

for _ in range(T):
    N = int(input())
    C = [int(i) for i in input().split()]

    S = sum(C)
    prime_factor = fact_prime_factors[S].copy()
    for c in C:
        for k, v in fact_prime_factors[c].items():
            prime_factor[k] -= v

    ret = 1
    for k, v in prime_factor.items():
        ret = ret * pow(k, v, M) % M

    print(ret)
