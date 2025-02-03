H, W = map(int, input().split())
S = [input() for _ in range(H)]

d = ((0, 1), (1, 0), (0, -1), (-1, 0))

def valid(y, x) :
  return 0 <= y < H and 0 <= x < W

ret = 4
for y in range(H) :
  for x in range(W) :
    if S[y][x] == '.': continue
    for i, (dy, dx) in enumerate(d) :
      for j, (ddy, ddx) in enumerate(d) :
        if i % 2 == j % 2 : continue
        if valid(y + ddy, x + ddx) and S[y + ddy][x + ddx] == '.' and valid(y + dy, x + dx) and S[y + dy][x + dx] == '#' and valid(y + ddy + dy, x + ddx + dx) and S[y + ddy + dy][x + ddx + dx] == '#' :
          ret += 1
          
print(ret)