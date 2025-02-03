N = [int(i) % 3 for i in str(input())]
mod = sum(N) % 3

if mod == 0 :
  print(0)
elif mod == 1 :
  if N.count(1) >= 1 and len(N) > 1 :
    print(1)
  elif N.count(2) >= 2 and len(N) > 2 :
    print(2)
  else :
    print(-1)
else :
  if N.count(2) >= 1 and len(N) > 1 :
    print(1)
  elif N.count(1) >= 2 and len(N) > 2 :
    print(2)
  else :
    print(-1)