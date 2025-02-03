S = input().split()

ret = []
for s in S :
  if s == 'Left' :
    ret.append('<')
  elif s == 'Right' :
    ret.append('>')
  else :
    ret.append('A')
    
print(' '.join(ret))