N = int(input())

prime = [2, 3]
i = 5
while 2 * i**3 <= N:
    for p in prime:
        if i % p == 0:
            break
        if p * p > i:
            prime.append(i)
            break
    i += 2

ret = 0
i = 0
for j in range(len(prime) - 1, -1, -1):
    while i < len(prime) and prime[i] * prime[j] ** 3 <= N:
        i += 1
    ret += min(i, j)
print(ret)
