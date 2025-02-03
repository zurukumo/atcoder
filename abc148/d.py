N = int(input())
a = [int(i) for i in input().split()]

pre = 0
for i in range(N) :
  if a[i] == pre + 1 :
    pre += 1

if pre == 0 :
  print(-1)
else :
  print(N - pre)