N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

imos = [0] * (10**6 + T)

for a in A:
    imos[a - 1] += 1
    imos[a - 1 + T] -= 1

for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

ret = 0
for i in imos:
    if i:
        ret += 1
print(ret)
