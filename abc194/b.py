N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

ret = float('inf')
for i in range(N):
  for j in range(N):
    if i == j:
      ret = min(ret, sum(AB[i]))
    else :
      ret = min(ret, max(AB[i][0], AB[j][1]))
      ret = min(ret, max(AB[j][0], AB[i][1]))
      
print(ret)