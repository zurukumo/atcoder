import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
UV = [[int(i) for i in input().split()] for _ in range(M)]
S = input()

vec = [[] for _ in range(N)]
for u, v in UV:
    vec[u - 1].append(v - 1)
    vec[v - 1].append(u - 1)

mem = [[(float("inf"), None), (float("inf"), None)] for _ in range(N)]


def update(cost, fr, i):
    if i == fr:
        return False
    if mem[i][0][1] == fr:
        if cost < mem[i][0][0]:
            mem[i][0][0] = cost
            return True
        else:
            return False
    elif mem[i][1][1] == fr:
        if cost < mem[i][1][0]:
            mem[i][1][0] = cost
            mem[i].sort()
            return True
        else:
            return False

    new_mem = mem[i].copy() + [(cost, fr)]
    new_mem.sort()
    new_mem.pop()
    if mem[i] != new_mem:
        mem[i] = new_mem
        return True
    else:
        return False


queue = collections.deque()
for i in range(N):
    if S[i] == "S":
        queue.append((0, i, i))

while queue:
    cost, fr, cur = queue.popleft()
    cost *= -1
    for nex in vec[cur]:
        ncost = cost + 1
        if update(ncost, fr, nex):
            queue.append((-ncost, fr, nex))

for i in range(N):
    if S[i] == "D":
        print(mem[i][0][0] + mem[i][1][0])
