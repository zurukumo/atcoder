N = int(input())
S = [list(input()) for _ in range(N)]

ret = 0
for i in range(N) :
    for j in range(N - 1, -1, -1) :
        if S[i][j] == '.' :
            ret += 1
            if i == N - 1 :
                break
            for k in range(j, N) :
                S[i+1][k] = 'o'
            break
                
print(ret)