S = input()

def judge() :
  for i, c in enumerate(S) :
    if i % 2 == 0 and not (ord('a') <= ord(c) <= ord('z')) :
      return 'No'
    if i % 2 == 1 and not (ord('A') <= ord(c) <= ord('Z')) :
      return 'No'
  
  return 'Yes'
  
print(judge())