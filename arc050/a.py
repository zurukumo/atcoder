R, B = map(int, input().split())
x, y = map(int, input().split())

ok, ng = 0, 10 ** 19
while ng - ok > 1 :
  n = (ok + ng) // 2
  r, b = R - n, B - n
  if r < 0 or b < 0 or r // (x - 1) + b // (y - 1) < n :
    ng = n
  else :
    ok = n

print(ok)