# 素因数分解
def prime_factor(x) :
  ret = dict()
  if x % 2 == 0 :
    ret[2] = 0
    while x % 2 == 0 :
      x //= 2
      ret[2] += 1
          
  i = 3
  while i * i <= x :
    if x % i == 0 :
      ret[i] = 0
      
      while x % i == 0 :
        x //= i
        ret[i] += 1
    i += 2
      
  if x != 1 :
    ret[x] = 1
  
  return ret
  
#素数列挙
primes = [2]
for i in range(3, N + 1, 2):
  flag = True
  for p in primes:
    if p * p > i :
      break
    if i % p == 0 : 
      flag = False
      break
  if flag : 
    primes.append(i)