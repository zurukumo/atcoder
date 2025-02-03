from collections import defaultdict
from itertools import permutations

N = int(input())
S = input()

pos = defaultdict(lambda: [])
for i, s in enumerate(S) :
  pos[s].append(i)

ret = 0
for a, b, c in (permutations('RGB')) :
  for center in pos[b] :
    cnt = [0] * (N + 1)
    left, right = 0, 0
    for l in pos[a] :
      if l >= center :
        break
      cnt[center-l] += 1
      left += 1
    for r in pos[c][::-1] :
      if r <= center :
        break
      cnt[r-center] += 1
      right += 1
    ret += left * right - cnt.count(2)
     

  
print(ret)