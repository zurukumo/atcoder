import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
C = [int(input()) for _ in range(N)]

ret = 0
for i in range(N) :
  cnt = 0
  for j in range(N) :
    if i == j :
      continue
    if C[i] % C[j] == 0 :
      cnt += 1
      
  if cnt % 2 == 0 :
    a, b = cnt // 2 + 1, cnt // 2
    ret += a / (a + b)
  else :
    ret += 0.5
    
print(ret)