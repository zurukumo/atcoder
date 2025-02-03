S = input()

n = ''
for s in S :
  if 48 <= ord(s) <= 57 :
    n += s
    
print(int(n))