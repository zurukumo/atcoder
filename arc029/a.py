N = int(input())
t = [int(input()) for _ in range(N)]

ret = float('inf')
for i in range(1 << N) :
    a, b = 0, 0
    for j in range(N) :
        if i & (1 << j) :
            a += t[j]
        else :
            b += t[j]
    ret = min(ret, max(a, b))
    
print(ret)