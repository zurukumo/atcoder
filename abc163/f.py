import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

N = int(input())
c = [int(i) - 1 for i in input().split()]
vec = [[] for _ in range(N)]
for _ in range(N - 1) :
  a, b = map(int, input().split())
  vec[a - 1].append(b - 1)
  vec[b - 1].append(a - 1)

ret = [N * (N - 1) // 2 + N] * N

par = [[N + i] for i in range(N)]
vec2 = [[] for _ in range(N * 2)]
have = [0] * (N * 2)
way = [0] * (N * 2)
fr = [0] * (N + 2)

for i in range(N, 2 * N) :
  have[i] = N + 1

mem = defaultdict(int)

def dfs(cur, pre) :
  s = 1
  ancestor = par[c[cur]][-1]
  vec2[ancestor].append(cur)
  if pre != -1 :
    fr[cur] = way[ancestor]
  par[c[cur]].append(cur)
  for nex in vec[cur] :
    if nex == pre : continue
    way[cur] = nex
    s += dfs(nex, cur)
    mem[(cur, nex)] = have[nex]
  par[c[cur]].pop()
  have[cur] = s
  return s
  
dfs(0, -1)

for i in range(N, 2 * N) :
  mem[(i, 0)] = N

for i in range(N) :
  q = [(N + i, -1)]
  while q :
    cur, pre = q.pop()
    for nex in vec2[cur] :
      mem[(cur, fr[nex])] -= have[nex]
      q.append((nex, cur))

for k, v in mem.items() :
  if v <= 0: continue
  if k[0] >= N :
    ret[k[0] % N] -= v * (v - 1) // 2 + v
  else :
    ret[c[k[0]]] -= v * (v - 1) // 2 + v
  
for i in range(N) :
  print(ret[i])