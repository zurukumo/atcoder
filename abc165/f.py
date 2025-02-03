import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from bisect import bisect_left

N = int(input())
a = [int(i) for i in input().split()]
vec = [[] for _ in range(N)]
for _ in range(N - 1) :
  u, v = map(int, input().split())
  vec[u - 1].append(v - 1)
  vec[v - 1].append(u - 1)

lis = [a[0]]
ret = [0] * N
def dfs(cur, pre) :
  for nex in vec[cur] :
    if nex == pre : continue
    if a[nex] > lis[-1] :
      lis.append(a[nex])
      ret[nex] = len(lis)
      dfs(nex, cur)
      lis.pop()
    else :
      pos = bisect_left(lis, a[nex])
      v = lis[pos]
      lis[pos] = a[nex]
      ret[nex] = len(lis)
      dfs(nex, cur)
      lis[pos] = v

dfs(0, -1)

ret[0] = 1
for i in range(N) :
  print(ret[i])