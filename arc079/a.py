N = int(input())
a = [int(i) for i in input().split()]

ng, ok = -1, sum(a)

while ok - ng > 1 :
    m = (ok + ng) // 2
    
    for i in range(-N, 1) :
        if m + i <= ng :
            continue
            
        c = 0
        for j in range(N) :
            c += (a[j] + m + i - N) // (N + 1) + 1
        if c <= m + i :
            ok = m + i
            break
    else :
        ng = m
        
print(ok)