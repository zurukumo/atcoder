import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
p = [int(input()) for _ in range(N - 1)]

vec = [[] for _ in range(N)]
for i in range(N - 1) :
  vec[i + 1].append(p[i])
  vec[p[i]].append(i + 1)

subtree = [0] * N

def dfs(cur, pre) :
  s = 0
  for nex in vec[cur] :
    if nex == pre : continue
    x = dfs(nex, cur)
    subtree[cur] = max(subtree[cur], x)
    s += x
  subtree[cur] = max(subtree[cur], N - 1 - s)
  
  return s + 1
  
dfs(0, -1)

for i in range(N) :
  print(subtree[i])