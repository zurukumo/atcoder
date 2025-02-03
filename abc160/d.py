from collections import deque

N, X, Y = map(int, input().split())

ret = [0] * N

vec = [[] for _ in range(N)]
for i in range(N - 1) :
  vec[i].append(i + 1)
  vec[i + 1].append(i)
vec[X - 1].append(Y - 1)
vec[Y - 1].append(X - 1)
  
for i in range(N) :
  dist = [-1] * N
  dist[i] = 0
  q = deque([i])
  while q :
    cur = q.popleft()
    cd = dist[cur]
    for nex in vec[cur] :
      if dist[nex] != -1 : continue
      q.append(nex)
      dist[nex] = cd + 1
  
  for i in range(N) :
    ret[dist[i]] += 1
    
    
for i in range(1, N) :
  print(ret[i] // 2)