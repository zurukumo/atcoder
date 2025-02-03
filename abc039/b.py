X = int(input())

l, r = 0, X + 1
while True :
    m = (l + r) // 2
    m4 = m**4
    
    if m4 > X :
        r = m
    elif m4 < X :
        l = m
    else :
        break
        
print(m)