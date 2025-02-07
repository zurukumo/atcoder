N = int(input())

MOD = 10**9 + 7

pfac = [1] * (N + 1)

for i in range(1, N + 1):
    j = i
    while j % 2 == 0:
        j //= 2
        pfac[2] += 1

    k = 3
    while j > 1:
        while j % k == 0:
            j //= k
            pfac[k] += 1
        k += 2

ret = 1
for i in range(2, N + 1):
    ret *= pfac[i]
    ret %= MOD

print(ret)
