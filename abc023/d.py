N = int(input())
HS = [[int(i) for i in input().split()] for _ in range(N)]

ng, ok = 0, 10 ** 25
while ok - ng > 1 :
  m = (ok + ng) // 2
  y = [(m - HS[i][0]) / HS[i][1] for i in range(N)]
  y.sort()
  for i in range(N) :
    if y[i] < i :
      ng = m
      break
  else :
    ok = m

print(ok)