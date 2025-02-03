N, M = map(int, input().split())

mod = 10 ** 9 + 7

fac = [1]
for i in range(1, N + M + 10) :
  fac.append(fac[-1] * i % mod)
inv = [pow(fac[-1], mod - 2, mod)]
for i in range(N + M + 9, 0, -1) :
  inv.append(inv[-1] * i % mod)
inv = inv[::-1]

def comb(n, r) :
  if n >= r and r >= 0 :
    return fac[n] * inv[n - r] * inv[r] % mod
  return 1
  
ret = 0
for i in range(N + 1) :
  if i % 2 == 1 :
    sign = -1
  else :
    sign = 1
  x = sign * comb(M, i) * comb(N, i) * fac[i] % mod
  x *= (fac[M - i] ** 2) * (inv[M - N] ** 2) % mod
  ret += x % mod
  ret %= mod
print(ret)