N = int(input())
vec = [[] for _ in range(N)]
for _ in range(N - 1) :
  a, b = map(int, input().split())
  vec[a-1].append(b-1)
  vec[b-1].append(a-1)

que = [(0, -1, 0)]
Mi, Mv = 0, 0
while que :
  cur, pre, dist = que.pop()
  if dist > Mv :
    Mi, Mv = cur, dist
  for nex in vec[cur] :
    if nex == pre :
      continue
    que.append((nex, cur, dist + 1))

que = [(Mi, -1, 1)]
Mi, Mv = 0, 0
while que :
  cur, pre, dist = que.pop()
  if dist > Mv :
    Mi, Mv = cur, dist
  for nex in vec[cur] :
    if nex == pre :
      continue
    que.append((nex, cur, dist + 1))

if Mv % 3 != 2 :
  print('First')
else :
  print('Second')