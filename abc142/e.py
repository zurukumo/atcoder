N, M = map(int, input().split())

ret = [float('inf')] * (1 << N)
for _ in range(M) :
    a, b = map(int, input().split())
    c = 0
    for i in input().split() :
        c |= 1 << (int(i) - 1)
    ret[c] = min(ret[c], a)

for i in range(1 << N) :
    if ret[i] == float('inf') :
        continue
    for j in range(1 << N) :
        k = i | j
        ret[k] = min(ret[k], ret[i] + ret[j])

if ret[-1] == float('inf') :
    print(-1)
else :
    print(ret[-1])