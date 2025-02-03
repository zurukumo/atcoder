N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]
cd = [[int(i) for i in input().split()] for _ in range(M)]

for a, b in ab :
    mi, mv = 0, float('inf')
    for i, (c, d) in enumerate(cd) :
        if abs(a-c) + abs(b-d) < mv :
            mi = i
            mv = abs(a-c) + abs(b-d)
    print(mi+1)