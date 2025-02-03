from collections import deque

N = int(input())
v = [[] for _ in range(N)]
for _ in range(N-1) :
  A, B = map(int, input().split())
  v[A-1].append(B-1)
  v[B-1].append(A-1)

q = deque([(0, -1)])
dist = [0] * N
while q :
  cur, pre = q.popleft()
  for nex in v[cur] :
    if nex == pre :
      continue
    q.append((nex, cur))
    dist[nex] = dist[cur] + 1

Md = max(dist)
Mi = dist.index(Md)

q = deque([(Mi, -1)])
dist = [0] * N
while q :
  cur, pre = q.popleft()
  for nex in v[cur] :
    if nex == pre :
      continue
    q.append((nex, cur))
    dist[nex] = dist[cur] + 1

print(Mi + 1, dist.index(max(dist)) + 1)