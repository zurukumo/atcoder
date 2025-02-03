N = int(input())

if N == 3 :
    print(2, 5, 63)
    
elif N == 4 :
    print(2, 5, 20, 63)
    
else :
    ret = [2, 4, 6]
    
    i = 3
    while N - len(ret) >= 2 and i + 6 <= 30000 :
        ret.append(i)
        ret.append(i + 6)
        i += 12

    i = 8
    while N - len(ret) >= 3 and i + 4 <= 30000 :
        ret.append(i)
        ret.append(i + 2)
        ret.append(i + 4)
        i += 6
        
    if N - len(ret) == 2 :
        ret.append(29996)
        ret.append(29998)
        
    elif N - len(ret) == 1 :
        ret.append(30000)
            
    print(*ret)