import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
A = [int(i) for i in input().split()]


primes = [2]
for i in range(3, 10**5 + 1, 2):
    flag = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            flag = False
            break
    if flag:
        primes.append(i)

divs = set()
for a in A:
    i = 0
    while i < len(primes) and primes[i] ** 2 <= a:
        while a % primes[i] == 0:
            a //= primes[i]
            divs.add(primes[i])
        i += 1
    if a != 1:
        divs.add(a)

muls = [True] * (M + 1)
for d in divs:
    i = d
    while i <= M:
        muls[i] = False
        i += d

ret = [i for i, r in enumerate(muls) if r][1:]

print(len(ret))
for r in ret:
    print(r)
