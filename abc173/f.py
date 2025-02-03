N = int(input())
uv = [[int(i) for i in input().split()] for _ in range(N - 1)]

e = 0
for u, v in uv :
  e += min(u, v) * (N - max(u, v) + 1)

v = 0
for i in range(1, N + 1) :
  v += i * (N + 1 - i)
  
print(v - e)