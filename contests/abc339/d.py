import collections
import sys

input = sys.stdin.readline

N = int(input())
S = [input() for _ in range(N)]

pos = []
field = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            field[i].append(1)
        elif S[i][j] == "P":
            field[i].append(0)
            pos.append((i, j))
        else:
            field[i].append(0)


visited = set()
visited.add((pos[0], pos[1]))

queue = collections.deque([(0, pos[0], pos[1])])
while queue:
    d, p1, p2 = queue.popleft()
    if p1 == p2:
        print(d)
        exit()

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        np1 = (p1[0] + dy, p1[1] + dx)
        np2 = (p2[0] + dy, p2[1] + dx)
        if not (0 <= np1[0] < N and 0 <= np1[1] < N) or field[np1[0]][np1[1]] == 1:
            np1 = p1
        if not (0 <= np2[0] < N and 0 <= np2[1] < N) or field[np2[0]][np2[1]] == 1:
            np2 = p2

        if (np1, np2) in visited:
            continue

        visited.add((np1, np2))
        queue.append((d + 1, np1, np2))

print(-1)
