A, B, C, D = map(int, input().split())

if C * D - B > 0:
  print((A + C * D - B - 1) // (C * D - B))
else:
  print(-1)