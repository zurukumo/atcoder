N = int(input())

def S(x) :
    ret = 0
    while x :
        ret += x % 10
        x //= 10
    return ret

if N % S(N) == 0 :
    print('Yes')
else :
    print('No')