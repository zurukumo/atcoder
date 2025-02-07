import collections

import sortedcontainers

N, X, Y = map(int, input().split())
A = [int(i) for i in input().split()]

mem = collections.defaultdict(lambda: collections.deque())
sl = sortedcontainers.SortedList()

ret = 0
j = 0
for i in range(N):
    sl.add(A[i])
    mem[A[i]].append(i)
    while sl and (sl[0] < Y or sl[-1] > X):
        sl.remove(A[j])
        mem[A[j]].popleft()
        j += 1

    if sl and sl[0] == Y and sl[-1] == X:
        ret += min(mem[X][-1], mem[Y][-1]) - j + 1

print(ret)
