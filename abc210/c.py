from collections import defaultdict

N, K = map(int, input().split())
c = [int(i) for i in input().split()]

kinds = defaultdict(int)
s = 0
for i in range(K):
  if kinds[c[i]] == 0:
    s += 1
  kinds[c[i]] += 1

ret = s
for i in range(K, N):
  kinds[c[i - K]] -= 1
  if kinds[c[i - K]] == 0:
    s -= 1
  if kinds[c[i]] == 0:
    s += 1
  kinds[c[i]] += 1
  ret = max(ret, s)
  
print(ret)