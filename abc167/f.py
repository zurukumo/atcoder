N = int(input())
S = [input() for _ in range(N)]

def solve() :
  T = []
  for s in S :
    open = 0
    close = 0
    for c in s :
      if c == ')' :
        if open > 0 :
          open -= 1
        else :
          close += 1
      else :
        open += 1
    T.append((open, close))
  
  if sum(op - cl for op, cl in T) != 0 :
    return 'No'
  
  inc = []
  dec = []
  for op, cl in T :
    if op >= cl :
      inc.append((cl, op))
    else :
      dec.append((op, cl))
      
  inc.sort()
  open = 0
  for cl, op in inc :
    if open >= cl :
      open += op - cl
    else :
      return 'No'
  
  close = 0
  dec.sort()
  for op, cl in dec :
    if close >= op :
      close += cl - op
    else :
      return 'No'
      
  return 'Yes'
      
print(solve())