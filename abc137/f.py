import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

p = int(input())
a = [int(i) for i in input().split()]

ret = [0] * p
fac = [1]
inv = [1]
for i in range(1, p):
    fac.append(fac[-1] * i % p)
    inv.append(pow(fac[-1], p - 2, p))

for i in range(p):
    if a[i] == 0:
        continue
    ret[0] += 1
    power = 1
    for j in range(p - 1, -1, -1):
        ret[j] += -fac[p - 1] * inv[p - 1 - j] * inv[j] * power % p
        ret[j] %= p
        power *= -i
        power %= p
print(" ".join(map(str, ret)))
