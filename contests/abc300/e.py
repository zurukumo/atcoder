N = int(input())

mod = 998244353

fac = [1]
inv = [pow(1, mod - 2, mod)]
for i in range(1, 1000):
    fac.append(fac[i - 1] * i % mod)
    inv.append(pow(fac[i], mod - 2, mod))


two = 0
three = 0
five = 0
while N % 2 == 0:
    N //= 2
    two += 1
while N % 3 == 0:
    N //= 3
    three += 1
while N % 5 == 0:
    N //= 5
    five += 1

if N != 1:
    print(0)
    exit()

ret = 0
for e in range(min(two, three) + 1):
    for c in range(two // 2 + 1):
        a = two - 2 * c - e
        b = three - e
        d = five
        if a < 0 or b < 0:
            continue

        s = a + b + c + d + e

        prob = fac[s]
        prob = prob * inv[a] % mod
        prob = prob * inv[b] % mod
        prob = prob * inv[c] % mod
        prob = prob * inv[d] % mod
        prob = prob * inv[e] % mod
        prob = prob * pow(pow(5, mod - 2, mod), s, mod) % mod
        ret += prob
        ret %= mod
print(ret)
