import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]

# point, number
ranks = [(0, i) for i in range(2 * N)]
for m in range(M):
    new_ranks = []
    for i in range(0, 2 * N, 2):
        p1, n1 = ranks[i]
        p2, n2 = ranks[i + 1]
        if (A[n1][m], A[n2][m]) in [("G", "C"), ("C", "P"), ("P", "G")]:
            p1 += 1
        if (A[n2][m], A[n1][m]) in [("G", "C"), ("C", "P"), ("P", "G")]:
            p2 += 1
        new_ranks.append((p1, n1))
        new_ranks.append((p2, n2))
    new_ranks.sort(key=lambda x: (-x[0], x[1]))
    ranks = new_ranks

for _, i in ranks:
    print(i + 1)
