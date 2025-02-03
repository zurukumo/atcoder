N, K = map(int, input().split())
xy = [[int(i) for i in input().split()] for _ in range(N)]

ret = float('inf')
for i in range(N) :
    for j in range(i, N) :
        for k in range(j, N) :
            for l in range(k, N) :
                x, y = zip(xy[i], xy[j], xy[k], xy[l])
                mx, Mx = min(x), max(x)
                my, My = min(y), max(y)
                
                counter = 0
                for m in range(N) :
                    if mx <= xy[m][0] <= Mx and my <= xy[m][1] <= My :
                        counter += 1
                if counter >= K :
                    ret = min(ret, (Mx-mx)*(My-my))
print(ret)