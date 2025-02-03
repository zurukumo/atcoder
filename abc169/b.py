N = int(input())
A = [int(i) for i in input().split()]

if 0 in A :
  print(0)
else :
  ret = 1
  for i in range(N) :
    ret *= A[i]
    if ret > 10 ** 18 :
      print(-1)
      break
  else :
    print(ret)