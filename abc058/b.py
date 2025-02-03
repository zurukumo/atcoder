O = input()
E = input()

ret = []
for i in range(len(O)) :
    ret.append(O[i])
    if i < len(E) :
        ret.append(E[i])
        
print(''.join(ret))