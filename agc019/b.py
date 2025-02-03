from collections import Counter

A = input()

cnt = Counter(A)

ret = len(A) * (len(A) - 1) // 2 + 1
for v in cnt.values() :
  ret -= v * (v - 1) // 2

print(ret)