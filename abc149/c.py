X = int(input())

primes = [2]
for i in range(3, 10**5 + 1000, 2):
    chk = True
    for p in primes:
        if p * p > i:
            break
        if i % p == 0:
            chk = False
            break
    if chk == True:
        primes.append(i)
        # print(primes)

for p in primes:
    if p >= X:
        print(p)
        break
