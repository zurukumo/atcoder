N = int(input())
a = [int(i) for i in input().split()]

def gcd(a, b) :
  if b > a : 
    a, b = b, a
  
  while b != 0 :
    a, b = b, a % b
  return a
  
ret = a[0]
for i in range(1, N) :
  ret = gcd(ret, a[i])
print(ret)