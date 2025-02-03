from heapq import heappop, heappush

first, last = input().split()
N = int(input())
s = [first, last] + [input() for _ in range(N)]

N += 2
M = len(s[0])
vec = [[] for _ in range(N)]

for i in range(N) :
  for j in range(i + 1, N) :
    if sum([s[i][k] != s[j][k] for k in range(M)]) <= 1 :
      vec[i].append(j)
      vec[j].append(i)

q = [(0, 0)]
dist = [float('inf')] * N
pre = [-1] * N
dist[0] = 0

while q :
  co, cur = heappop(q)
  if co > dist[cur] :
    continue
  for nex in vec[cur] :
    if dist[nex] > co + 1 :
      heappush(q, (co + 1, nex))
      dist[nex] = co + 1
      pre[nex] = cur

if dist[1] == float('inf') :
  print(-1)
else :
  print(dist[1] - 1)
  word = []
  cur = 1
  while cur != 0 :
    word.append(s[cur])
    cur = pre[cur]
  word.append(s[0])
  for w in word[::-1] :
    print(w)