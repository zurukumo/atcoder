from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

cnt = Counter(A)
mem = dict()
for k, v in cnt.items() :
  mem[k] = v * (v - 1) // 2

s = sum(mem.values())
for i in range(N) :
  ret = s - mem[A[i]] + (cnt[A[i]] - 1) * (cnt[A[i]] - 2) // 2
  print(ret)