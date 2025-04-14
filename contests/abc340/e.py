import atcoder.lazysegtree

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

lst = atcoder.lazysegtree.LazySegTree(
    lambda a, b: a + b,
    0,
    lambda f, x: f + x,
    lambda f, g: f + g,
    0,
    A,
)

for b in B:
    x = lst.get(b)
    m = (b + x) % N
    if m < b:
        lst.apply(0, m + 1, x // N + 1)
        lst.apply(m + 1, b + 1, x // N)
        lst.apply(b + 1, N, x // N + 1)
    else:
        lst.apply(0, b + 1, x // N)
        lst.apply(b + 1, m + 1, x // N + 1)
        lst.apply(m + 1, N, x // N)
    lst.apply(b, b + 1, -x)


ret = [lst.get(i) for i in range(N)]
print(*ret)
