x, y = map(int, input().split())

if abs(x) < abs(y) :
    if x >= 0 :
        if y >= 0 :
            print(- x + y)
        else :
            print(- x - y + 1)
    else :
        if y >= 0 :
            print(x + y + 1)
        else :
            print(x - y + 2)
elif abs(x) == abs(y) :
    if x * y < 0 :
        print(1)
    else :
        print(0)
else :
    if x > 0 :
        if y > 0 :
            print(x - y + 2)
        else :
            print(x + y + 1)
    else :
        if y > 0 :
            print(- x - y + 1)
        else :
            print(- x + y)