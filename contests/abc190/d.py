N = int(input())


def prime_factor(x):
    ret = dict()
    if x % 2 == 0:
        ret[2] = 0
        while x % 2 == 0:
            x //= 2
            ret[2] += 1

    i = 3
    while i * i <= x:
        if x % i == 0:
            ret[i] = 0

            while x % i == 0:
                x //= i
                ret[i] += 1
        i += 2

    if x != 1:
        ret[x] = 1

    return ret


pf = prime_factor(N)
ret = 1
for k, v in pf.items():
    if k == 2:
        continue

    ret *= v + 1

print(ret * 2)
