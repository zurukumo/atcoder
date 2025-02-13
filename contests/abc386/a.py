import collections

A, B, C, D = map(int, input().split())

counter = collections.Counter([A, B, C, D])
values = sorted(counter.values())
if values == [1, 3] or values == [2, 2]:
    print("Yes")
else:
    print("No")
