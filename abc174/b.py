N, D = map(int, input().split())
XY = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for X, Y in XY :
  if X * X + Y * Y <= D * D :
    ret += 1
print(ret)