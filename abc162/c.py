K = int(input())

def gcd(a, b) :
  if b > a : 
    a, b = b, a
  
  while b != 0 :
    a, b = b, a % b
  return a

ret = 0

x = [0] * (K + 1)
for a in range(1, K + 1) :
  for b in range(1, K + 1) :
    x[gcd(a, b)] += 1

for c in range(1, K + 1) :
  for d in range(1, K + 1) :
    ret += gcd(c, d) * x[d]
    
print(ret)