import collections

A = [int(i) for i in input().split()]

counter = collections.Counter(A)
print(sum(v // 2 for v in counter.values()))
