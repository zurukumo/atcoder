N, M = map(int, input().split())
A = [int(i) for i in input().split()]

pos = [set() for _ in range(N)]
pos[0] = set(range(M))

for i in range(M):
    a = A[i] - 1
    pos[a], pos[a + 1] = pos[a + 1], pos[a]

    if i in pos[a]:
        pos[a].remove(i)
        pos[a + 1].add(i)
    elif i in pos[a + 1]:
        pos[a + 1].remove(i)
        pos[a].add(i)

ret = [0] * M
for i in range(N):
    for j in pos[i]:
        ret[j] = i + 1

print(*ret)
