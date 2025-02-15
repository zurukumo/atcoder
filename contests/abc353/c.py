import sortedcontainers

N = int(input())
A = [int(i) for i in input().split()]

ret = 0
sl = sortedcontainers.SortedList(A)
s = sum(A)
for a in A:
    sl.remove(a)
    s -= a
    ret += a * len(sl) + s
    over = len(sl) - sl.bisect_left(10**8 - a)
    ret -= over * 10**8
print(ret)
