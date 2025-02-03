from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

mod = 10 ** 9 + 7

cnt = Counter(A)
if cnt[0] != 1 or A[0] != 0 :
  print(0)

else :
  ret = 1
  for i in range(1, max(A) + 1) :
    ret *= pow(pow(2, cnt[i-1], mod) - 1, cnt[i], mod) * pow(2, cnt[i] * (cnt[i] - 1) // 2, mod) % mod
    ret %= mod

  print(ret)