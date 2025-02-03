from itertools import combinations

N, M = map(int, input().split())
vec = [[] for _ in range(N)]
for _ in range(M) :
  x, y = map(int, input().split())
  vec[x-1].append(y-1)
  vec[y-1].append(x-1)

ret = 0
for i in range(1 << N) :
  member = []
  for j in range(N) :
    if i & (1 << j) :
      member.append(j)
  for a, b in combinations(member, 2) :
    if not b in vec[a] :
      break
  else :
    ret = max(ret, bin(i)[2:].count('1'))

print(ret)