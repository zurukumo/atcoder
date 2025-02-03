N, M = map(int, input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

def judge() :
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            flg = True
            for k in range(M) :
                for l in range(M) :
                    if A[i+k][j+l] != B[k][l] :
                        flg = False
                        break
                    if not flg :
                        break
            if flg :
                return 'Yes'
                    
    return 'No'
    
print(judge())