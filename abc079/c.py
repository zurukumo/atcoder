ABCD = list(map(int, input()))

for i in range(8) :
    ret = ABCD[0]
    for j in range(3) :
        if (i >> j) & 1 :
            ret += ABCD[j+1]
        else :
            ret -= ABCD[j+1]
    
    if ret == 7 :
        op1 = '+' if (i >> 0) & 1 else '-'
        op2 = '+' if (i >> 1) & 1 else '-'
        op3 = '+' if (i >> 2) & 1 else '-'
        print('{}{}{}{}{}{}{}=7'.format(ABCD[0], op1, ABCD[1], op2, ABCD[2], op3, ABCD[3]))
        break