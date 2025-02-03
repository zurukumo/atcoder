N, K = map(int, input().split())
P = [int(i) - 1 for i in input().split()]
C = [int(i) for i in input().split()]

ret = -float('inf')
done = set()
for n in range(N) :
  if n in done : continue
    
  cur = n
  s = C[cur]
  done.add(cur)
  loop = [n]
  while not P[cur] in done :
    cur = P[cur]
    done.add(cur)
    loop.append(cur)
    s += C[cur]
  
  if s <= 0:
    for i in loop :
      cur = i
      x = 0
      for _ in range(min(len(loop), K)) :
        cur = P[cur]
        x += C[cur]
        ret = max(ret, x)
  else :
    d = 0
    k = K
    if k > len(loop) :
      d = s * (k // len(loop) - 1)
      k = k % len(loop) + len(loop)
      
    for i in loop :
      cur = i
      x = 0
      for _ in range(k) :
        cur = P[cur]
        x += C[cur]
        ret = max(ret, x + d)
      
print(ret)
