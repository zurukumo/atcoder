R, C, K = map(int, input().split())
s = [[0 if i == 'o' else 1 for i in input()] for _ in range(R)]
dia = [[1] * C for _ in range(R)]

for i in range(R) :
    for j in range(C) :
        if s[i][j] :
            for di in range(max(-i, -K+1), min(R-i, K)) :
                for dj in range(max(-j, -K+1+abs(di)), min(C-j, K-abs(di))) :
                    dia[i+di][j+dj] = 0

ret = 0
for i in range(K-1, R-K+1) :
    for j in range(K-1, C-K+1) :
        ret += dia[i][j]

print(ret)