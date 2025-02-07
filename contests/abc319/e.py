N, X, Y = map(int, input().split())
PT = [[int(i) for i in input().split()] for _ in range(N - 1)]
Q = int(input())
q = [int(input()) for _ in range(Q)]

cost = [0] * 840
for i in range(840):
    s = i
    for p, t in PT:
        if s % p != 0:
            s += p - s % p
        s += t
    cost[i] = s - i

for start in q:
    s = start + X
    s += cost[s % 840]
    s += Y
    print(s)
