N, K = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(N)]

ab.sort()
for i in range(N) :
    a, b = ab[i]
    if K > b :
        K -= b
    else :
        print(a)
        break