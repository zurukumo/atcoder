N, S, K = map(int, input().split())
PQ = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for p, q in PQ:
    ret += p * q

if ret < S:
    ret += K

print(ret)
