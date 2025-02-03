N, x = map(int, input().split())

if x == 1 or x == 2 * N - 1 :
    print('No')

else :
    print('Yes')
    l, r = [1], [2*N-1]
    
    i = 2 * N - 2
    while len(l) < N - 1 :
        if i != x :
            l.append(i)
        i -= 1
    
    i = 2
    while len(r) < N - 1 :
        if i != x :
            r.append(i)
        i += 1
        
    for i in l[::-1] + [x] + r :
        print(i)
    