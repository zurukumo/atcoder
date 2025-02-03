N = int(input())
abcde = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for i in range(N) :
  ret = max(ret, sum(abcde[i][:4]) + abcde[i][4] * 110 / 900)
  
print(ret)