from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

c = Counter(A)
ret = 0
for k in c.keys():
  ret += c[k] * (N - c[k])
  
print(ret // 2)