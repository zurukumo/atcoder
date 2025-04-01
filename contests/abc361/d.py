import collections

N = int(input())
S = input()
T = input()

S += ".."
T += ".."

queue = collections.deque()
queue.append(S)
cost = collections.defaultdict(int)
cost[S] = 0
while queue:
    cur = queue.popleft()
    empty_pos = cur.index(".")
    for i in range(0, N + 1):
        if cur[i] != "." and cur[i + 1] != ".":
            nex = list(cur)
            nex[i : i + 2], nex[empty_pos : empty_pos + 2] = nex[empty_pos : empty_pos + 2], nex[i : i + 2]
            nex = "".join(nex)
            if nex not in cost:
                cost[nex] = cost[cur] + 1
                queue.append(nex)

print(cost[T] if T in cost else -1)
