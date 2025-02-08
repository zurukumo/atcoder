import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

mod = 10**9 + 7


def gcd(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a % b
    return a


p = []
both = 0
zeroa = 0
zerob = 0
for a, b in AB:
    if a == 0 and b == 0:
        both += 1
        continue
    elif a == 0:
        zeroa += 1
        continue
    elif b == 0:
        zerob += 1
        continue

    g = gcd(abs(a), abs(b))
    a //= g
    b //= g
    if a < 0:
        a *= -1
        b *= -1
    p.append((a, b))

ret = 1
visited = set()
cnt = Counter(p)
for k, v in cnt.items():
    a, b = k
    c, d = b, -a
    if c < 0:
        c *= -1
        d *= -1
    if cnt[(c, d)] == 0:
        ret *= pow(2, v, mod)
    else:
        if not (c, d) in visited:
            u = cnt[(c, d)]
            ret *= pow(2, u, mod) + pow(2, v, mod) - 1
            visited.add((a, b))
            visited.add((c, d))
    ret %= mod

ret *= pow(2, zeroa, mod) + pow(2, zerob, mod) - 1
ret %= mod

print((ret - 1 + both) % mod)
