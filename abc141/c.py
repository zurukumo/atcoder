N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

point = [0] * N
for a in A :
    point[a-1] += 1
    
for i in range(N) :
    if K - Q + point[i] > 0 :
        print('Yes')
    else :
        print('No')