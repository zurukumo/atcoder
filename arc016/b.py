N = int(input())
x = [list(input()) for _ in range(N)]

ret = 0
for i in range(N) :
    for j in range(9) :
        if x[i][j] == 'x' :
            ret += 1
        elif x[i][j] == 'o' and (i == 0 or x[i-1][j] != 'o') :
            ret += 1
            
print(ret)