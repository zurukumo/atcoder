import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

K = int(input())

cnt = 0
def dfs(keta, cur) :
  if keta == 0 :
    global cnt
    cnt += 1
    if cnt == K :
      print(cur)
      exit()
    return 
      
  i = cur % 10
  if i - 1 >= 0 :
    dfs(keta - 1, cur * 10 + i - 1)
  dfs(keta - 1, cur * 10 + i)
  if i + 1 <= 9 :
    dfs(keta - 1, cur * 10 + i + 1)

for keta in range(100) :
  for i in range(1, 10) :
    dfs(keta, i)