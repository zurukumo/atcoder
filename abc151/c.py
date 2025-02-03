from collections import defaultdict

N, M = map(int, input().split())
pS = [input().split() for _ in range(M)]

ac, wa = 0, 0
solved = defaultdict(int)
warning = defaultdict(int)

for p, S in pS :
  if solved[p] == 1 :
    continue
    
  if S == 'WA' :
    warning[p] += 1
    
  else :
    ac += 1
    solved[p] = 1
    wa += warning[p]
    
print(ac, wa)