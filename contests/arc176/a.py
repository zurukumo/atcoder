N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(M)]

mod = set()
for a, b in AB:
    mod.add((a - 1 + b - 1) % N)

i = 0
while len(mod) < M:
    mod.add(i)
    i += 1

print(N * M)
for i in range(N):
    for m in mod:
        j = (m - i) % N
        print(i + 1, j + 1)
