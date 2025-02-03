N = int(input())
A = [int(i) for i in input().split()]

A.sort(reverse=True)
ret = A[0]
c = N - 2
i = 1
while c :
  if c >= 2 :
    ret += A[i] * 2
    c -= 2
  else :
    ret += A[i]
    c -= 1
  i += 1

print(ret)