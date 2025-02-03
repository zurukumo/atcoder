import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

N = int(input())
C = [int(i) for i in input().split()]
AB = [[int(i) for i in input().split()] for _ in range(N - 1)]

vec = [[] for _ in range(N)]
for A, B in AB :
  A -= 1
  B -= 1
  vec[A].append(B)
  vec[B].append(A)

color = defaultdict(int)
ret = []
def dfs(cur, pre):
  if color[C[cur]] == 0 :
    ret.append(cur)
  color[C[cur]] += 1
  for nex in vec[cur]:
    if nex == pre :
      continue
    dfs(nex, cur)
  color[C[cur]] -= 1
  
dfs(0, -1)  

ret.sort()
for r in ret :
  print(r + 1)