from atcoder import lazysegtree

N = int(input())
S = input()
Q = int(input())

v = []
for c in S:
    if c == "A":
        v.append(1)
    else:
        v.append(-1)
for i in range(1, N):
    v[i] += v[i - 1]

T = list(S)

rmq = lazysegtree.LazySegTree(lambda a, b: min(a, b), float("inf"), lambda f, x: f + x, lambda f, g: f + g, 0, v)
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        i = int(query[1]) - 1
        c = query[2]
        if c == "A" and T[i] == "B":
            rmq.apply(i, N, 2)
            T[i] = "A"
        if c == "B" and T[i] == "A":
            rmq.apply(i, N, -2)
            T[i] = "B"
    else:
        l = int(query[1]) - 1
        r = int(query[2]) - 1
        m = rmq.prod(l, r + 1)
        base = rmq.get(l - 1) if l - 1 >= 0 else 0
        if m - base < 0:
            print("No")
        else:
            print("Yes")
