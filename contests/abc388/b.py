N, D = map(int, input().split())
TL = [[int(i) for i in input().split()] for _ in range(N)]

for d in range(1, D + 1):
    ret = 0
    for t, l in TL:
        ret = max(ret, t * (l + d))
    print(ret)
