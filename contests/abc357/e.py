from collections import deque

N = int(input())
a = [int(i) - 1 for i in input().split()]

global_seen = set()
group = [-1] * N


def bfs(start):
    cur = start

    if cur in global_seen:
        return

    local_seen = set()
    history = deque([])

    history.append(cur)
    local_seen.add(cur)
    global_seen.add(cur)

    while True:
        cur = a[cur]
        if cur in local_seen:
            while history[0] != cur:
                history.popleft()

            for h in history:
                group[h] = len(history)
            return

        elif cur in global_seen:
            return
        else:
            history.append(cur)
            local_seen.add(cur)
            global_seen.add(cur)


for i in range(N):
    bfs(i)


rev = [[] for _ in range(N)]
for i, x in enumerate(a):
    rev[x].append(i)

queue = []
for i in range(N):
    if group[i] != -1:
        queue.append(i)


while queue:
    cur = queue.pop()
    for nex in rev[cur]:
        if group[nex] == -1:
            group[nex] = group[cur] + 1
            queue.append(nex)

print(sum(group))
