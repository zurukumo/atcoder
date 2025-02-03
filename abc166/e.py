from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]

l1 = Counter([i + 1 - A[i]for i in range(N)])
l2 = Counter([i + 1 + A[i]for i in range(N)])

ret = 0
for k, v in l1.items() :
  ret += v * l2[k]
  
print(ret)
