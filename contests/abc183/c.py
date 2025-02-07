from itertools import permutations

N, K = map(int, input().split())
T = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for perm in permutations(range(1, N), N - 1):
    c = 0
    for i in range(N - 2):
        c += T[perm[i]][perm[i + 1]]
    c += T[0][perm[0]]
    c += T[perm[-1]][0]

    if c == K:
        ret += 1

print(ret)
