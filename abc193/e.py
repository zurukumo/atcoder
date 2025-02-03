def ext_gcd(a, b, p, q):
  if b == 0:
    return 1, 0, a
    
  q, p, d = ext_gcd(b, a % b, q, p)
  q -= a//b * p
  return p, q, d
  
def crt(b1, m1, b2, m2):
  p, q, d = ext_gcd(m1, m2, 0, 0)
  if (b2 - b1) % d != 0:
    return (0, -1)
    
  m = m1 * (m2 // d)
  tmp = (b2 - b1) // d * p % (m2 // d)
  r = (b1 + m1 * tmp) % m
  return (r, m)
  
T = int(input())
XYPQ = [[int(i) for i in input().split()] for _ in range(T)]

for X, Y, P, Q in XYPQ:
  ret = float('inf')
  for x in range(X, X + Y) :
    for p in range(P, P + Q) :
      r, m = crt(x, 2 * (X + Y), p, P + Q)
      if m != -1 :
        ret = min(ret, r)

  if ret == float('inf') :
    print('infinity')
  else :
    print(ret)

