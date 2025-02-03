N = int(input())
C = [int(i) for i in input().split()]

mod = 10 ** 9 + 7

C.sort()
ret = 1
for i, c in enumerate(C):
  if c <= i:
    ret = 0
  else:
    ret *= c - i
    ret %= mod
    
print(ret)