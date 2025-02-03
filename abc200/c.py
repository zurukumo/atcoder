from collections import defaultdict

N = int(input())
A = [int(i) for i in input().split()]

dic = defaultdict(int)
for a in A :
  dic[a % 200] += 1

ret = 0
for k in dic:
  v = dic[k]
  ret += v * (v - 1) // 2
  
print(ret)