n, k = map(int, input().split())

mod = 10 ** 9 + 7

fac = [1]
for i in range(1, 2 * n + 1) :
  fac.append(fac[-1] * i % mod)
inv = [pow(fac[-1], mod - 2, mod)]
for i in range(2 * n, 0, -1) :
  inv.append(inv[-1] * i % mod)
  
inv = inv[::-1]

def comb(n, r) :
  if n < 1 or n < r : return 0
  return fac[n] * inv[r] * inv[n-r] % mod
  
ret = comb(n + n - 1, n)
for i in range(1, n - k) :
  ret -= comb(n - 1, k + i) * comb(n, k + i)
  ret %= mod
print(ret % mod)