D, G = map(int, input().split())
pc = [[int(i) for i in input().split()] for _ in range(D)]

ret = float('inf')
for i in range(2 ** D) :
    g = G
    last = 0
    count = 0
    for j in range(D) :
        if i % 2 == 0 :
            last = j
        else :
            g -= pc[j][0] * (j + 1) * 100 + pc[j][1]
            count += pc[j][0]
        i //= 2
    
    if pc[last][0] * (last + 1) * 100 <= g :
        continue
        
    if g <= 0 :
        ret = min(ret, count)
    else :
        count += -(-g // ((last + 1) * 100))
        ret = min(ret, count)
        
print(ret)