N, Q = map(int, input().split())
C = [int(i) for i in input().split()]

colors = [set([C[i]]) for i in range(N)]
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if len(colors[a]) > len(colors[b]):
        colors[a] |= colors[b]
        colors[b] = colors[a]
        colors[a] = set()
    else:
        colors[b] |= colors[a]
        colors[a] = set()
    print(len(colors[b]))
