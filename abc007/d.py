A, B = map(int, input().split())

def f(X) :
  X = [int(i) for i in str(X)]
  a, b = 0, 1
  for x in X :
    if 4 < x <= 9 :
      a = a * 8 + b * (x - 1)
    else :
      a = a * 8 + b * x
    
    if x == 4 or x == 9 :
      b = 0
      
  return a + b

print(B - (A - 1) - (f(B) - f(A - 1)))