import collections
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)


N, M = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(2 * M)][1::2]


counter = collections.defaultdict(list)
queue = list(range(M))

while queue:
    i = queue.pop()
    if len(a[i]) > 0:
        x = a[i].pop()
        counter[x].append(i)
        if len(counter[x]) == 2:
            queue.append(counter[x][0])
            queue.append(counter[x][1])
            N -= 1

if N == 0:
    print("Yes")
else:
    print("No")
