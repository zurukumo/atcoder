from collections import Counter

n = int(input())
v = [int(i) for i in input().split()]

o = v[::2]
e = v[1::2]
co = list(Counter(o).items()) + [(-1, 0)]
ce = list(Counter(e).items()) + [(-2, 0)]
co.sort(key=lambda x: x[1], reverse=True)
ce.sort(key=lambda x: x[1], reverse=True)

if co[0][0] == ce[0][0] :
    print(min(n - co[0][1] - ce[1][1], n - co[1][1] - ce[0][1]))
else :
    print(n - co[0][1] - ce[0][1])