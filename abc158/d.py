S = input()
Q = int(input())

prefix = ''
suffix = ''
mode = 0
for _ in range(Q) :
  Query = list(input().split())
  if Query[0] == '1' :
    mode ^= 1
  else :
    _, F, C = Query
    F = int(F) - 1
    
    if mode != F :
      suffix += C
    else :
      prefix += C
      

if mode == 0 :
  print(prefix[::-1] + S + suffix)
else :
  print(suffix[::-1] + S[::-1] + prefix)