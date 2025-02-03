N, M = map(int, input().split())
PY = [[int(i) for i in input().split()] for _ in range(M)]

iPY = []
for i, (P, Y) in enumerate(PY) :
    iPY.append((i, P, Y))
iPY.sort(key=lambda x: x[2])

ret = [0] * M
counter = [0] * N
for i, P, _ in iPY :
    counter[P-1] += 1
    ret[i] = '{:06d}'.format(P) + '{:06d}'.format(counter[P-1])

for i in range(M) :
    print(ret[i])