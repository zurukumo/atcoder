N, M = map(int, input().split())
KA = [[int(i) for i in input().split()] for _ in range(N)]

ret = [0] * (M + 1)
for i in range(N) :
    for j in KA[i][1:] :
        ret[j] += 1
print(ret.count(N))