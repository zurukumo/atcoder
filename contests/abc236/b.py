import collections

N = int(input())
A = [int(i) for i in input().split()]

counter = collections.Counter(A)
for k, v in counter.items():
    if v == 3:
        print(k)
