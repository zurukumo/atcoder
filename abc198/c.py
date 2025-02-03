R, X, Y = map(int, input().split())

def judge():
  a = X ** 2 + Y ** 2
  b = R ** 2
  for i in range(10 ** 6):
    if i * i * b > a :
      if i == 1 :
        return 2
      else :
        return i
    if i * i * b == a :
      return i
      
print(judge())