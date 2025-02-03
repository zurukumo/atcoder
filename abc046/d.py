s = input()

ret = 0
g, p = 0, 0
for s_ in s :
    if s_ == 'g' :
        if p < g :
            p += 1
            ret += 1
        else :
            g += 1
    else :
        if p < g :
            p += 1
        else :
            g += 1
            ret -= 1
            
print(ret)