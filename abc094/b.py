N, M, X = map(int, input().split())
A = [int(i) for i in input().split()]

u, l = 0, 0
for a in A :
    if a > X :
        u += 1
    elif a < X :
        l += 1
        
print(min(u, l))
    