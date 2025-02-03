A, B, C, K = map(int, input().split())

if A >= K :
  ret = K
else :
  ret = A
  K -= A
  K -= B
  if K > 0 :
    ret -= K
    
print(ret)