N, M, D = map(int, input().split())
A = [int(i) for i in input().split()]

x = list(range(N))
for a in A:
    x[a - 1], x[a] = x[a], x[a - 1]

y = list(range(N))
while D:
    if D & 1:
        y = [x[y[i]] for i in range(N)]
    x = [x[x[i]] for i in range(N)]
    D >>= 1

ret = [0] * N
for i in range(N):
    ret[y[i]] = str(i + 1)

print("\n".join(ret))
