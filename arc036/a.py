N, K = map(int, input().split())
t = [int(input()) for _ in range(N)]

for i in range(2, N) :
  if sum(t[i-2:i+1]) < K :
    print(i + 1)
    break
else :
  print(-1)