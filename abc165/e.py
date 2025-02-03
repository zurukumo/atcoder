N, M = map(int, input().split())

# 左パート
l, r = 1, N // 2
while M and l < r :
  print(l, r)
  l += 1
  r -= 1
  M -= 1
  
# 右パート
l, r = N // 2 + 2 - N % 2, N
while M :
  print(l, r)
  l += 1
  r -= 1
  M -= 1