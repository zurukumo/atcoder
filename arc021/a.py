A = [[int(i) for i in input().split()] for _ in range(4)]

flag = False
for y in range(4) :
  for x in range(4) :
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
      nx, ny = x + dx, y + dy
      if 0 <= nx < 4 and 0 <= ny < 4 and A[y][x] == A[ny][nx] :
        flag = True
        
if flag :
  print('CONTINUE')
else :
  print('GAMEOVER')