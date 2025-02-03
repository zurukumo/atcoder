N = int(input())
RH = [[int(i) for i in input().split()] for _ in range(N)]

rh = [[0] * 4 for _ in range(100001)]
for R, H in RH :
    rh[R][0] += 1
    rh[R][H] += 1

for i in range(1, 100001) :
    rh[i][0] += rh[i-1][0]
    
for R, H in RH :
    cor = [0, 2, 3, 1]
    w = rh[R-1][0] + rh[R][cor[H]]
    d = rh[R][H] - 1
    l = N - w - d - 1
    print(w, l, d)