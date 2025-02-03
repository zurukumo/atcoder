N = int(input())

ret = set()
for i in range(2, 10 ** 10) :
  if i * i > N :
    break
    
  x = i * i
  while x <= N :
    ret.add(x)
    x *= i

print(N - len(ret))
  