N, M = map(int, input().split())

imos = [0] * (10 ** 5 + 2)

for _ in range(M) :
    L, R = map(int, input().split())
    imos[L] += 1
    imos[R+1] -= 1

for i in range(10 ** 5 + 1) :
    imos[i+1] += imos[i]

print(imos.count(M))