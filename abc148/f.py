from collections import deque

N, u, v = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(N - 1) :
  A, B = map(int, input().split())
  vec[A - 1].append(B - 1)
  vec[B - 1].append(A - 1)

du = [0] * N
pu = [-1] * N
q = [(u - 1, -1)]
while q :
  cur, pre = q.pop()
  for nex in vec[cur] :
    if nex != pre :
      du[nex] = du[cur] + 1
      pu[nex] = cur
      q.append((nex, cur))

dv = [0] * N
pv = [-1] * N
q = [(v - 1, -1)]
while q :
  cur, pre = q.pop()
  for nex in vec[cur] :
    if nex != pre :
      dv[nex] = dv[cur] + 1
      pv[nex] = cur
      q.append((nex, cur))

# du[u - 1] = 2
# dv[v - 1] = 2

ret = 0
for i, (u, v) in enumerate(zip(du, dv)) :
  if u < v or (u == v and pu[i] != pv[i]) :
    if u == v :
      ret = max(ret, u)
    else :
      ret = max(ret, v - 1)
print(ret)