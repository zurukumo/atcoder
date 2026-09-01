from atcoder import segtree

N, D = map(int, input().split())
A = [int(i) for i in input().split()]


ret = [1] * N

M = 5 * 10**5 + 10
v = [0] * M
rmq = segtree.SegTree(lambda a, b: max(a, b), -float("inf"), v)
for a in A:
    l = max(a - D, 0)
    r = min(a + D, M - 1)
    x = rmq.prod(l, r + 1)
    rmq.set(a, x + 1)


print(rmq.prod(0, M))
