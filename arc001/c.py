c = []

def good(x, y) :
    for (xx, yy) in c :
        if x == xx : return False
        if y == yy : return False
        if x - xx == y - yy or x - xx == yy - y : return False
    return True
    
for i in range(8) :
    for j, v in enumerate(input()) :
        if v == 'Q' :
            if good(i, j) :
                c.append((i, j))
            else :
                print('No Answer')
                exit()
        
def rec() :
    if len(c) == 8 :
        return True
        
    for i in range(8) :
        for j in range(8) :
            if good(i, j) :
                c.append((i, j))
                if rec() :
                    return True
                c.pop()
                
    return False

rec()

if len(c) == 8 :
    ret = [['.' for _ in range(8)] for _ in range(8)]
    for x, y in c :
        ret[x][y] = 'Q'
    for r in ret :
        print(''.join(r))
else :
    print('No Answer')