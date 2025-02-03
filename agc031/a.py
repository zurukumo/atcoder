from collections import Counter

N = int(input())
S = input()
mod = 10 ** 9 + 7

c = Counter(S)
ret = 1
for v in c.values() :
  ret *= v + 1
  ret %= mod
  
print(ret - 1)