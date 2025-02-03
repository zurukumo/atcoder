N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]
M = int(input())
op = [input() for _ in range(M)]
Q = int(input())
AB = [[int(i) for i in input().split()] for _ in range(Q)]

#info [is_x, xflag, yflag, xp, yp]
info = []
is_x = True
xflag = True
yflag = True
xp = 0
yp = 0
for operation in op :
  # print(operation)
  if 1 <= int(operation[0]) <= 2 :
    p = int(operation[0])
    q = 0
  else :
    p, q = operation.split()
    p = int(p)
    q = int(q)
    
  # print('pq', p, q)
    
  if p == 1 :
    is_x = not is_x
    xflag, yflag = yflag, not xflag
    xp, yp = yp, -xp
  if p == 2 :
    is_x = not is_x
    xflag, yflag = not yflag, xflag
    xp, yp = -yp, xp
  if p == 3 :
    xflag = not xflag
    xp = 2 * q - xp
  if p == 4 :
    yflag = not yflag
    yp = 2 * q - yp
    
  info.append([is_x, xflag, yflag, xp, yp])
info.append([True, True, True, 0, 0])
  
# print('info')
# for i in info :
  # print(i)
  
# print()
# AB = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1]]
for A, B in AB :
  x, y = xy[B - 1]
  # print(x, y)
  # print(op[A - 1])
  is_x, xflag, yflag, xp, yp = info[A - 1]
  # print(info[A - 1])
  
  if not is_x :
    y, x = x, y
  if not xflag :
    x *= -1
  if not yflag :
    y *= -1
  x += xp
  y += yp
  print(x, y)
  # print()