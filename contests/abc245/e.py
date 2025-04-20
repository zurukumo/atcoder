import sortedcontainers

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
D = [int(i) for i in input().split()]

chocolates = []
for i in range(N):
    chocolates.append((A[i], B[i]))
chocolates.sort()

boxes = []
for i in range(M):
    boxes.append((C[i], D[i]))
boxes.sort()

ds = sortedcontainers.SortedList()

while chocolates:
    a, b = chocolates.pop()

    while boxes and boxes[-1][0] >= a:
        c, d = boxes.pop()
        ds.add(d)

    idx = ds.bisect_left(b)
    if idx == len(ds):
        print("No")
        exit()

    ds.pop(idx)

print("Yes")
