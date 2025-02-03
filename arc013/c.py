N = int(input())

ret = 0
for _ in range(N) :
  X, Y, Z = map(int, input().split())
  M = int(input())
  seq = [float('inf')] * 6
  for _ in range(M) :
    x, y, z = map(int, input().split())
    seq[0] = min(seq[0], x)
    seq[1] = min(seq[1], X - (x + 1))
    seq[2] = min(seq[2], y)
    seq[3] = min(seq[3], Y - (y + 1))
    seq[4] = min(seq[4], z)
    seq[5] = min(seq[5], Z - (z + 1))
  for i in range(6) :
    ret ^= seq[i]

if ret != 0 :
  print('WIN')
else :
  print('LOSE')