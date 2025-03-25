import sortedcontainers

N = int(input())
P = [int(i) for i in input().split()]

sc = sortedcontainers.SortedList(range(N))
xs = []
for p in P[::-1]:
    p -= 1
    xs.append(sc.pop(p))

ret = [0] * N
for i, x in enumerate(xs[::-1]):
    ret[x] = i + 1

print(*ret)
