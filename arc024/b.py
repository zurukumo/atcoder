from collections import Counter

L, R = map(int, input().split())
l = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

ret = 0
cnt = Counter(l)
for i in range(R) :
  if cnt[r[i]] >= 1 :
    ret += 1
    cnt[r[i]] -= 1
    
print(ret)