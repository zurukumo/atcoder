import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import defaultdict

N, X = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(N - 1) :
  x, y, c = map(int, input().split())
  vec[x - 1].append((y - 1, c))
  vec[y - 1].append((x - 1, c))

memo = defaultdict(int)
def dfs(pre, cur, x) :
  memo[x] += 1
  for nex, c in vec[cur] :
    if nex == pre : continue
    dfs(cur, nex, x ^ c)
    
dfs(-1, 0, 0)

keys = list(memo.keys())

ret = 0
for k in keys :
  if k == k ^ X :
    ret += memo[k] * (memo[k] - 1)
  else :
    ret += memo[k] * memo[k^X]
print(ret // 2)