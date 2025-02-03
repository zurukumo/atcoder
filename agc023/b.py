N = int(input())
S = [list(input()) for _ in range(N)]

def check(a) :
    for i in range(N) :
        for j in range(i, N) :
            if S[(a+i)%N][j] != S[(a+j)%N][i] :
                return False
                
    return True

ret = 0
for a in range(N) :
    if check(a) :
        ret += N
            
print(ret)