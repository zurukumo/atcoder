N, K = map(int, input().split())

if K > (N - 1) * (N - 2) // 2 :
    print(-1)
else :
    t = (N - 1) * (N - 2) // 2 - K
    print(N + t - 1)
    for i in range(1, N) :
        print(i, N)

    i, j = 1, 2
    while t > 0 :
        print(i, j)
        
        j += 1
        if j == N :
            i, j = i + 1, i + 2
        t -= 1