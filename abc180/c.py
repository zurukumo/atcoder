N = int(input())

l = []
r = []
for i in range(1, N + 1):
  if i * i > N:
    break
    
  if N % i == 0:
    l.append(i)
    if i * i != N:
      r.append(N // i)
      
ret = l + r[::-1]
for r in ret:
  print(r)
