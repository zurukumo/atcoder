N, M = map(int, input().split())
a = []
for _ in range(M):
    C = int(input())
    a.append([int(i) for i in input().split()])

ret = 0
for bit in range(1, 1 << M):
    group = set()
    for i in range(M):
        if bit & (1 << i):
            group |= set(a[i])
    if len(group) == N:
        ret += 1
print(ret)
