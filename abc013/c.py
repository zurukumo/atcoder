N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

ret = float('inf')
for x in range(N + 1) :
  y = max(0, (N * E - H - (B + E) * x) // (D + E) + 1)
  if 0 <= x + y <= N :
    ret = min(ret, A * x + C * y)
    
print(ret)