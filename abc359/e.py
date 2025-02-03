from sortedcontainers import SortedList

N = int(input())
H = [int(i) for i in input().split()]

h_with_index = [(i + 1, h) for i, h in enumerate(H)]
h_with_index.sort(key=lambda x: x[1], reverse=True)

ret = [0] * (N + 1)
sc = SortedList()
sc.add(0)

for i, h in h_with_index:
    j = sc[sc.bisect_left(i) - 1]
    ret[i] = ret[j] + h * (i - j)
    sc.add(i)

print(*[a + 1 for a in ret[1:]])
