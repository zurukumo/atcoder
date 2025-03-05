H, W, N = map(int, input().split())
A = [int(i) for i in input().split()]

queue = [(H, W)]
A.sort(reverse=True)

for a in A:
    mk, mv = None, float("inf")
    for i, (h, w) in enumerate(queue):
        if h >= 2**a and w >= 2**a and min(h - 2**a, w - 2**a) < mv:
            mk = i
            mv = min(h - 2**a, w - 2**a)

    if mk is None:
        print("No")
        exit()

    h, w = queue.pop(mk)
    if h < w:
        h1 = h - 2**a
        w1 = 2**a
        if h1 > 0:
            queue.append((h1, w1))
        h2 = h
        w2 = w - 2**a
        queue.append((h2, w2))
    else:
        h1 = 2**a
        w1 = w - 2**a
        if w1 > 0:
            queue.append((h1, w1))
        h2 = h - 2**a
        w2 = w
        queue.append((h2, w2))

print("Yes")
