N = int(input())

ret = 0
for i in range(1, N) :
  ret += N / (N - i)
print(ret)