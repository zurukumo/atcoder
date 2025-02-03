A, B = map(int, input().split())


mod = 998244353

div = 1
primes = []
i = 2
while i * i <= A:
    c = 0
    while A != 1 and A % i == 0:
        c += 1
        A //= i

    if c > 0:
        primes.append((i, c))
        div *= B * c + 1

    i += 1

if A != 1:
    primes.append((A, 1))
    div *= B + 1

ret = float("inf")
for prime, c in primes:
    s = (B * c) * (B * c + 1) // 2
    rest = div // (B * c + 1)
    ret = min(ret, s * rest // c)


print(ret % mod)
