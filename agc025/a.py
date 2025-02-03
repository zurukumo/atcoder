N = int(input())

ret = float('inf')
for i in range(1, N) :
  ret = min(ret, sum(int(i) for i in str(i) + str(N - i)))

print(ret)