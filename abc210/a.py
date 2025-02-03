N, A, X, Y = map(int, input().split())

if N > A:
  print(X * A + (N - A) * Y)
else:
  print(X * N)