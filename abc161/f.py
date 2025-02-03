N = int(input())

div = set()
for i in range(1, N + 1) :
  if i * i > N : 
    break
    
  if N % i == 0 :
    div.add(i)
    if i != N // i :
      div.add(N // i)

N = N - 1
for i in range(1, N + 1) :
  if i * i > N : 
    break
    
  if N % i == 0 :
    div.add(i)
    if i != N // i :
      div.add(N // i)

def check(x) :
  n = N + 1
  while n >= x :
    if n % x == 0 :
      n //= x
    else :
      n %= x
      
  return n == 1

ret = 0
for x in list(div) :
  if x == 1 : continue
  if check(x) :
    ret += 1
      
print(ret)