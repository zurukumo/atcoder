N, M = map(int, input().split())
lrs = [[int(i) for i in input().split()] for _ in range(N)]

imos = [0] * (M + 1)
ret = 0
for l, r, s in lrs:
    imos[l - 1] += s
    imos[r] -= s
    ret += s

for i in range(1, M + 1):
    imos[i] += imos[i - 1]

print(ret - min(imos[:M]))
