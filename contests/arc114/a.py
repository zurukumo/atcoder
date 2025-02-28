N = int(input())
X = [int(i) for i in input().split()]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


ret = float("inf")
for bit in range(1 << len(primes)):
    tmp = 1
    for i in range(len(primes)):
        if bit & (1 << i):
            tmp *= primes[i]
    if all(gcd(tmp, x) != 1 for x in X):
        ret = min(ret, tmp)
print(ret)
