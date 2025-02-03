N = int(input())
D = [[int(i) for i in input().split()] for _ in range(N)]

def judge() :
  c = 0
  for a, b in D :
    if a == b : 
      c += 1
    else :
      c = 0
    if c >= 3 :
      return 'Yes'
  return 'No'
  
print(judge())