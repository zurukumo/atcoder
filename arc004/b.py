N = int(input())
d = [int(input()) for _ in range(N)]

l = d[0]
u = d[0]

for i in range(1, N) :        
    if d[i] > u :
        l = d[i] - u
    else :
        l = max(0, l - d[i])
        
    u += d[i]
    
print(u)
print(l)