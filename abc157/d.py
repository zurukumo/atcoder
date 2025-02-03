import sys
input = sys.stdin.readline
from collections import Counter

N, M, K = map(int, input().split())
friend = [[] for _ in range(N)]
for _ in range(M) :
  a, b = map(int, input().split())
  friend[a - 1].append(b - 1)
  friend[b - 1].append(a - 1)
block = [[] for _ in range(N)]
for _ in range(K) :
  c, d = map(int, input().split())
  block[c - 1].append(d - 1)
  block[d - 1].append(c - 1)
  
visited = [-1] * N
color = 0
for i in range(N) :
  if visited[i] == -1 :
    q = [i]
    visited[i] = color
    while q :
      cur = q.pop()
      for nex in friend[cur] :
        if visited[nex] >= 0 : continue
        visited[nex] = color
        q.append(nex)    
    color += 1
    
cnt = Counter(visited)

ret = []
for i in range(N) :
  s = cnt[visited[i]]
  for j in block[i] :
    if visited[i] == visited[j] :
      s -= 1
  ret.append(s - len(friend[i]) - 1)
  
print(*ret)