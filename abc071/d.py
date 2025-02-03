N = int(input())
S1 = input()
S2 = input()
mod = 10 ** 9 + 7

# False->tate True->yoko
if S1[0] == S2[0] :
    ret = 3
    pre = False
    i = 1
else :
    ret = 6
    pre = True
    i = 2

while i < N :
    cur = (S1[i] != S2[i])
    if not pre :
        ret *= 2
    elif pre and cur :
        ret *= 3
    
    ret %= mod
    
    if cur :
        i += 2
    else :
        i += 1
    pre = cur
    
print(ret)