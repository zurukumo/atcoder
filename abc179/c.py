N = int(input())

ret = 0
for a in range(1, N + 1) :
  ret += (N - 1) // a
  
print(ret)