N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N)]

iab = []
for i, (a, b) in enumerate(ab) :
  iab.append([i, a, b])

iab.sort(key=lambda x: x[1], reverse=True)

ret = []
INF = 1 << 60
l, r = INF, INF
for i, a, b in iab :
  if b <= l :
    l, r = a, b
    ret.append([i, a, b])
print(len(ret))
    
ret = [[-INF, -INF, -INF]] + ret[::-1] + [[INF, INF, INF]]

iab.sort(key=lambda x: x[2])
n = 1
for i, a, b in iab :
  while ret[n + 1][1] < b :
    n += 1
  if ret[n - 1][2] <= a and ret[n][0] > i :
    ret[n] = [i, a, b]

print(*[i + 1 for i, a, b in ret[1:-1]])