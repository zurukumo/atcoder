N, K = map(int, input().split())

ret = 0
while N != 0 :
  N //= K
  ret += 1
  
print(ret)