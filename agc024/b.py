N = int(input())
P = [int(input()) for _ in range(N)]

pos = [0] * N
for i in range(N) :
    pos[P[i] - 1] = i
    
ret = 0
c = 1
for i in range(1, N) :
    if pos[i] > pos[i - 1] :
        c += 1
    else :
        ret = max(ret, c)
        c = 1
ret = max(ret, c)
        
print(N - ret)