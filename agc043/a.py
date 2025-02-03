from heapq import heappush, heappop

H, W = map(int, input().split())
s = [[i == '.' for i in input()] for _ in range(H)]

dist = [[float('inf')] * W for _ in range(H)]
dist[0][0] = 0

h = [(0, 0, 0)]
while h :
  cc, cy, cx = heappop(h)
  for dy, dx in ((1, 0), (0, 1)) :
    ny, nx = cy + dy, cx + dx
    if 0 <= ny < H and 0 <= nx < W :
      nc = cc + (s[ny][nx] != s[cy][cx])
      if nc < dist[ny][nx] :
        heappush(h, (nc, ny, nx))
        dist[ny][nx] = nc
        
print((dist[H-1][W-1] + 2 - s[0][0] - s[-1][-1]) // 2)