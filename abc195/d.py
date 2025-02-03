N, M, Q = map(int, input().split())
WV = [[int(i) for i in input().split()] for _ in range(N)]
X = [int(i) for i in input().split()]
Query = [[int(i) - 1 for i in input().split()] for _ in range(Q)]


WV.sort(key=lambda x: x[1], reverse=True)

for L, R in Query:
  X2 = list(X[:L] + X[R + 1:])
  X2.sort()
  ret = 0
  for W, V in WV:
    for i, w in enumerate(X2):
      if w >= W :
        X2.pop(i)
        ret += V
        break
  print(ret)
  