s = input()

ret = float('inf')
for c in set(s) :
  tmp = 0
  t = s[::]
  u = ''
  while t.count(c) != len(t) :
    tmp += 1
    for i in range(len(t) - 1) :
      if t[i] == c or t[i+1] == c :
        u += c
      else :
        u += t[i]
    t = u[::]
    u = ''
  ret = min(ret, tmp)
  
print(ret)