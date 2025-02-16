import collections

A, B, C, D, E = map(int, input().split())

counter = collections.Counter([A, B, C, D, E])
if 2 in counter.values() and 3 in counter.values():
    print("Yes")
else:
    print("No")
