n = int(input())
a = [int(i) for i in input().split()]

def calc(sign) :
    pre_sign = sign
    s = 0
    ret = 0
    for ai in a :
        if ai + s > 0 :
            cur_sign = 1
        elif ai + s < 0 :
            cur_sign = -1
        else :
            cur_sign = 0
        
        if pre_sign * cur_sign < 0 :
            s += ai
        else :
            ret += abs((pre_sign * -1) - (ai + s))
            s = pre_sign * -1
        pre_sign *= -1
        
    return ret
    
print(min(calc(1), calc(-1)))