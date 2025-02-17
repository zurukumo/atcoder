import collections

N = int(input())

primes = [2, 3]
i = 5
while i <= N + 10:
    for p in primes:
        if p * p > i:
            primes.append(i)
            break
        if i % p == 0:
            break
    i += 2


def prime_factorization(n):
    factors = collections.defaultdict(int)
    for p in primes:
        if n == 1:
            break
        while n % p == 0:
            n //= p
            factors[p] += 1
    return factors


mem = collections.defaultdict(int)
for i in range(1, N + 1):
    key = []
    for k, v in prime_factorization(i).items():
        if v % 2 == 1:
            key.append(k)
    mem[tuple(key)] += 1

ret = 0
for k, v in mem.items():
    ret += v * v
print(ret)
