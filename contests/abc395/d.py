N, Q = map(int, input().split())

nests = list(range(N))
pos = list(range(N))
birds = list(range(N))

for _ in range(Q):
    op = list(map(int, input().split()))
    if op[0] == 1:
        _, a, b = op
        a -= 1
        b -= 1
        birds[a] = pos[b]
    elif op[0] == 2:
        _, a, b = op
        a -= 1
        b -= 1
        pos_a = pos[a]
        pos_b = pos[b]
        pos[a], pos[b] = pos_b, pos_a
        nests[pos_a], nests[pos_b] = nests[pos_b], nests[pos_a]
    else:
        _, a = op
        a -= 1
        print(nests[birds[a]] + 1)
