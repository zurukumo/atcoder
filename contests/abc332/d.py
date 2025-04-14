import collections

H, W = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(H)]
B = [[int(i) for i in input().split()] for _ in range(H)]


def check(hperm, wperm):
    for i in range(H):
        for j in range(W):
            if A[hperm[i]][wperm[j]] != B[i][j]:
                return False
    return True


ret = float("inf")
queue = collections.deque([(0, tuple(range(H)), tuple(range(W)))])
cost = collections.defaultdict(lambda: float("inf"))
cost[(tuple(range(H)), tuple(range(W)))] = 0
while queue:
    c, hperm, wperm = queue.popleft()
    if cost[(hperm, wperm)] < c:
        continue
    if check(hperm, wperm):
        ret = min(ret, c)
    for y in range(H - 1):
        new_hperm = list(hperm)
        new_hperm[y], new_hperm[y + 1] = new_hperm[y + 1], new_hperm[y]
        new_hperm = tuple(new_hperm)
        if cost[(new_hperm, wperm)] > c + 1:
            cost[(new_hperm, wperm)] = c + 1
            queue.append((c + 1, new_hperm, wperm))
    for x in range(W - 1):
        new_wperm = list(wperm)
        new_wperm[x], new_wperm[x + 1] = new_wperm[x + 1], new_wperm[x]
        new_wperm = tuple(new_wperm)
        if cost[(hperm, new_wperm)] > c + 1:
            cost[(hperm, new_wperm)] = c + 1
            queue.append((c + 1, hperm, new_wperm))


if ret == float("inf"):
    print(-1)
else:
    print(ret)
