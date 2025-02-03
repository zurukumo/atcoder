N = int(input())
a = [int(i) for i in input().split()]

ret = 0
for i in range(1, N) :
  if a[i] == a[i - 1] :
    a[i] = -1
    ret += 1

print(ret)