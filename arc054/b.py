import math
P = float(input())

def f(x) :
    return x + P / math.pow(2, x / 1.5)

l = 0
r = 100
for _ in range(100) :
    ml = l * 2 / 3 + r / 3
    mr = l / 3 + r * 2 / 3
    if f(ml) >= f(mr) :
        l = ml
    else :
        r = mr
        
print(f(r))