import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N - 1)]

vec = [[] for _ in range(N)]
for a, b in AB:
    vec[a - 1].append(b - 1)
    vec[b - 1].append(a - 1)


class Queue:
    def __init__(self):
        self.a = (-1, -1, -1)
        self.b = (-1, -1, -1)

    def push(self, x):
        if (x[1], x[0]) > (self.a[1], self.a[0]):
            self.b = self.a
            self.a = x
        elif (x[1], x[0]) > (self.b[1], self.b[0]):
            self.b = x

    def __iter__(self):
        return iter([self.a, self.b])


orders = [(0, -1, -1)]
queue = [(0, -1, -1)]
while queue:
    cur, pre, from_id = queue.pop()
    for from_id, nex in enumerate(vec[cur]):
        if nex == pre:
            continue
        orders.append((nex, cur, from_id))
        queue.append((nex, cur, from_id))

memos = [Queue() for _ in range(N)]
while orders:
    cur, pre, from_id = orders.pop()
    memos[cur].push((cur, 0, -1))
    if pre != -1:
        k, v, _ = memos[cur].a
        memos[pre].push((k, v + 1, from_id))


queue = [0]
done = [False] * N
done[0] = True

while queue:
    cur = queue.pop()
    for from_id, nex in enumerate(vec[cur]):
        if done[nex]:
            continue
        done[nex] = True
        queue.append(nex)
        for nk, nv, nfrom_id in memos[cur]:
            if nfrom_id == from_id:
                continue
            memos[nex].push((nk, nv + 1, -1))


for i in range(N):
    print(memos[i].a[0] + 1)
