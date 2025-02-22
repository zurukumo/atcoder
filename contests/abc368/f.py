N = int(input())
A = [int(i) for i in input().split()]

primes = [2, 3]
for i in range(5, 10**5 + 1, 2):
    for prime in primes:
        if prime * prime > i:
            primes.append(i)
            break
        if i % prime == 0:
            break


def factorize(x):
    ret = dict()
    for prime in primes:
        if prime * prime > x:
            break
        while x % prime == 0:
            x //= prime
            if prime in ret:
                ret[prime] += 1
            else:
                ret[prime] = 1
    if x != 1:
        if x in ret:
            ret[x] += 1
        else:
            ret[x] = 1
    return ret


bit = 0
for a in A:
    factors = factorize(a)
    cnt = 0
    for v in factors.values():
        cnt += v
    bit ^= cnt


if bit == 0:
    print("Bruno")
else:
    print("Anna")
