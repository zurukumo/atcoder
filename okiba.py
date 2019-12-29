N, K = map(int, input().split())

mod = 10 ** 9 + 7

div1 = []
div2 = []
i = 1
while i * i <= K :
  if K % i == 0 :
    div1.append(i)
    if i * i != K :
      div2.append(K // i)
  i += 1
      
divisor = div1 + div2[::-1]

def count_prime_factor(x) :
  ret = 1
  if x % 2 == 0 :
    while x % 2 == 0 :
      x //= 2
      ret += 1
      
  i = 3
  while i * i <= x :
    if x % i == 0 :
      while x % i == 0 :
        x //= i
        ret += 1
    i += 2
      
  if x != 1 :
    ret += 1
  
  return ret

cnt = dict()
for d in divisor :
  cnt[d] = count_prime_factor(d) % 2

print(divisor)

ret = 0
for div1 in divisor :
  if div1 > N :
    break
  x1 = N // div1
  s = x1 * (1 + x1) * div1 // 2
  print('div1', div1, 's', s, 'mod', cnt[div1])
  for div2 in divisor :
    if div2 > N :
      break
    if div2 > div1 and div2 % div1 == 0 :
      x2 = N // div2
      if cnt[div1] == cnt[div2] :
        s += x2 * (1 + x2) * div2 // 2
      else :
        s -= x2 * (1 + x2) * div2 // 2
      print('div2', div2, 'calc', x2 * (1 + x2) * div2 // 2, 's', s, 'mod', cnt[div2])
  print(div1, s // div1)
  print()
  ret += s // div1
  ret %= mod
  
print(ret * K % mod)

N, K = map(int, input().split())

from collections import defaultdict
from math import gcd

cnt = defaultdict(int)
for i in range(1, N + 1) :
  cnt[gcd(i, K)] += i
  
print(cnt)