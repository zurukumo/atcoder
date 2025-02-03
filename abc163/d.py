N, K = map(int, input().split())

mod = 10 ** 9 + 7
  
ret = 0
for i in range(K, N + 2) :
  ret += (2 * N - i + 1) * i // 2 - (i - 1) * i // 2 + 1
  ret %= mod
  
print(ret)