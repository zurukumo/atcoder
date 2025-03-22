import collections

A = [int(i) for i in input().split()]

cnt = collections.Counter(A)

over_2 = sum(1 for v in cnt.values() if v >= 2)
over_3 = sum(1 for v in cnt.values() if v >= 3)

if over_3 >= 1 and over_2 >= 2:
    print("Yes")
else:
    print("No")
