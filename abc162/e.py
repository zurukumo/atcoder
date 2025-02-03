N, K = map(int, input().split())

mod = 10 ** 9 + 7

def make_divisors(N) :
  divisors = []
  for i in range(1, N + 1) :
    if i * i > N :
      break
    if N % i == 0:
      divisors.append(i)
      if i != N // i:
        divisors.append(N // i)

  return divisors

cnt = [0] * (K + 1)

ret = 0
for i in range(K, 0, -1) :
  cnt[i] += pow(K // i, N, mod)
  ret += i * cnt[i] % mod
  ret %= mod
  for j in make_divisors(i) :
    if j == i :
      continue
    cnt[j] -= cnt[i]

print(ret)