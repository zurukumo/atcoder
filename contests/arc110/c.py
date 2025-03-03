N = int(input())
P = [int(i) for i in input().split()]

pos = [0] * N

for i, p in enumerate(P):
    pos[p - 1] = i

done = [False] * (N - 1)

ret = []
for i in range(N):
    x = pos[i]
    while x > i:
        if done[x - 1]:
            print(-1)
            exit()
        ret.append(x - 1)
        done[x - 1] = True
        P[x - 1], P[x] = P[x], P[x - 1]
        pos[P[x] - 1] = x
        pos[P[x - 1] - 1] = x - 1
        x -= 1

if P == list(range(1, N + 1)) and all(done):
    for i in ret:
        print(i + 1)
else:
    print(-1)
