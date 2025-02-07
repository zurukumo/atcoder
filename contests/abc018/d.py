from itertools import combinations

N, M, P, Q, R = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(R):
    x, y, z = map(int, input().split())
    vec[x - 1].append((y - 1, z))

ret = 0
for comb in combinations(range(N), P):
    tar = [0] * M
    for x in comb:
        for y, z in vec[x]:
            tar[y] += z
    tar.sort(reverse=True)
    ret = max(ret, sum(tar[:Q]))

print(ret)
