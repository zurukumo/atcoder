import collections

from atcoder.lazysegtree import LazySegTree

N = int(input())
A = [int(i) for i in input().split()]

dpl = [0] * N
dpr = [0] * N

s = set()
for i in range(N):
    s.add(A[i])
    dpl[i] = len(s)

s = set()
for i in range(N - 1, -1, -1):
    s.add(A[i])
    dpr[i] = len(s)

init = [0] * N
for i in range(N - 1):
    init[i] = dpl[i] + dpr[i + 1]

lst = LazySegTree(max, 0, lambda f, x: f + x, lambda f, g: f + g, 0, init)


ret = 0
pos = [collections.deque() for _ in range(N + 1)]
for i in range(N):
    pos[A[i]].append(i)

done = 0
for i in range(N):
    a = dpl[i]
    pos[A[i]].popleft()
    if len(pos[A[i]]) != 0:
        n = pos[A[i]][0]
        lst.apply(i + 1, n, -1)
    else:
        done += 1
    b = lst.prod(i + 1, N) - done
    ret = max(ret, a + b)


print(ret)
