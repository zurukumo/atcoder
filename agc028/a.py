N, M = map(int, input().split())
S = input()
T = input()

def gcd(a, b) :
    if b > a : 
        a, b = b, a
    
    while b != 0 :
        a, b = b, a % b
    return a
    
def lcm(a, b) :
    return a * b // gcd(a, b)

for i in range(N) :
  if i * M % N != 0 :
    continue
  if S[i] != T[i * M // N] :
    print(-1)
    break
else :
  print(lcm(N, M))
  
