N, K = map(int, input().split())

mod = 10**9 + 7

divs = []
i = 1
while i * i <= K:
    if K % i == 0:
        divs.append(i)
        if i * i != K:
            divs.append(K // i)
    i += 1
divs.sort()

k = K
prime_factors = []
if k % 2 == 0:
    prime_factors.append(2)
    while k % 2 == 0:
        k //= 2

i = 3
while i * i <= k:
    if k % i == 0:
        prime_factors.append(i)
        while k % i == 0:
            k //= i
    i += 2

if k != 1:
    prime_factors.append(k)

ret = 0
for d in divs:
    pfs = []
    for prime_factor in prime_factors:
        if K % (prime_factor * d) == 0:
            pfs.append(prime_factor)
    s = 0
    for mask in range(1 << len(pfs)):
        sgn = 1
        mul = 1
        for i in range(len(pfs)):
            if mask & (1 << i):
                sgn *= -1
                mul *= pfs[i]
        x = d * mul
        s += sgn * (x + N // x * x) * (N // x) // 2
    ret += s // d
    ret %= mod

print(ret * K % mod)
