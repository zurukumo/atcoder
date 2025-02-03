N, M = map(int, input().split())
abt = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[float('inf')] * N for _ in range(N)]
for a, b, t in abt :
  vec[a-1][b-1] = vec[b-1][a-1] = t
for i in range(N) :
  vec[i][i] = 0
  
for k in range(N) :
  for i in range(N) :
    for j in range(N) :
      vec[i][j] = min(vec[i][j], vec[i][k] + vec[k][j])
      
print(min(max(vec[i]) for i in range(N)))