N = int(input())

if N % 2 == 0 :
  ret = 0
  x = 10
  for _ in range(1, 40) :
    ret += N // x
    x *= 5
    
  print(ret)
else :
  print(0)