from collections import deque, defaultdict

H, W = map(int, input().split())
a = [[i for i in input()] for _ in range(H)]

dist = [[float('inf')] * W for _ in range(H)]

teleport = defaultdict(lambda : [])
for y in range(H) :
  for x in range(W) :
    if a[y][x] == 'S' :
      sy, sx = y, x
    if a[y][x] == 'G' :
      gy, gx = y, x
    if ord('a') <= ord(a[y][x]) <= ord('z') :
      teleport[a[y][x]].append((y, x))

h = deque([(0, sy, sx)])
dist[sy][sx] = 0
while h :
  ccost, cy, cx = h.popleft()
  if ccost > dist[cy][cx] :
    continue
  for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1) :
    ny, nx = cy + dy, cx + dx
    if not 0 <= ny < H or not 0 <= nx < W or a[ny][nx] == '#' :
      continue
    
    if ccost + 1 < dist[ny][nx] :
      h.append((ccost + 1, ny, nx))
      dist[ny][nx] = ccost + 1
      
  if ord('a') <= ord(a[cy][cx]) <= ord('z') :
    for ny, nx in teleport[a[cy][cx]] :
      if ccost + 1 < dist[ny][nx] :
        h.append((ccost + 1, ny, nx))
        dist[ny][nx] = ccost + 1
    teleport[a[cy][cx]] = []
    
if dist[gy][gx] == float('inf') :
  print(-1)
else :
  print(dist[gy][gx])