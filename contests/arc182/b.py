T = int(input())
for _ in range(T):
    N, K = map(int, input().split())

    old = [1]
    for _ in range(K - 1):
        new = []
        for o in old:
            new.append((o << 1) + 0)
        for o in old:
            new.append((o << 1) + 1)
        old = new[:N]

    while len(old) < N:
        old.append(1)

    print(*old)
