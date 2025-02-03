N, K = map(int, input().split())
a = [int(i) for i in input().split()]

x = K // N
K %= N

ret = [x] * N
b = sorted([[v, k] for k, v in enumerate(a)])
for v, k in b[:K]:
    ret[k] += 1

for r in ret:
    print(r)
