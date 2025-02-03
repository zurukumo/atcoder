from collections import deque

N = int(input())
at = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
x = [int(i) for i in input().split()]

y = [[x[i], i] for i in range(Q)]
y.sort()
z = deque(y)

lowerk, lowerv = 0, -float('inf')
upperk, upperv = 0, float('inf')
s = 0
for a, t in at:
  if t == 1:
    s += a
    lowerv += a
    upperv += a
    
  elif t == 2 :
    if lowerv <= a :
      lowerv = a
    if upperv <= a :
      lowerk += upperk
      upperk = 0
      upperv = a
    while z and z[0][0] + s <= a:
      lowerk += 1
      z.popleft()
    
  elif t == 3 :
    if upperv >= a:
      upperv = a
    if lowerv >= a:
      upperk += lowerk
      lowerk = 0
      lowerv = a
    while z and z[-1][0] + s >= a:
      upperk += 1
      z.pop()

  # print([lowerv] * lowerk)
  # print([s + i[0] for i in z])
  # print([upperv] * upperk)
  # print()

ret = []
ret += [lowerv] * lowerk
ret += [s + i[0] for i in z]
ret += [upperv] * upperk

ans = [0] * Q
for i in range(Q):
  ans[y[i][1]] = ret[i]
  
for i in range(Q):
  print(ans[i])