from collections import Counter

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

c = list(Counter(A).values())
c.sort()

ret = 0
for i in range(len(c)-K) :
    ret += c[i]
print(ret)