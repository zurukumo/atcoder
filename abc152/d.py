import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())

ret = 0
for i in range(1, N + 1) :
  l = str(i)[0]
  r = str(i)[-1]
  
  if r == '0' :
    continue
    
  if l == r and int(l) <= N :
    ret += 1
    
  for j in range(0, len(str(N)) - 2) :
    ret += pow(10, j)
  
  if str(N)[0] == r :
    if len(str(N)) >= 2 :
      ret += int(str(N)[1:]) // 10
      if int(str(N)[-1]) >= int(l) :
        ret += 1
  elif str(N)[0] > r :
    ret += pow(10, len(str(N)) - 2)
    
print(ret)