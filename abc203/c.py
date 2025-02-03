N, K = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

AB.sort()
pos = 0
mon = K
for A, B in AB:
  cost = A - pos
  if cost > mon:
    break
    
  pos = A
  mon -= cost
  mon += B
  
pos += mon

print(pos)