from collections import Counter
N = int(input())
a = [int(i) for i in input().split()]

c = Counter(a)
ret = 0
for k, v in c.items() :
    if v > k :
        ret += v - k
    elif v < k :
        ret += v
print(ret)