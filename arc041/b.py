x, y = map(int, input().split())
k = int(input())

if k > y :
  print(y + x + y - k)
else :
  print(x + k)