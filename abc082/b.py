s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

def solve() :
    flg = True
    for i in range(min(len(s), len(t))) :
        if ord(s[i]) < ord(t[i]) :
            return 'Yes'
        elif ord(s[i]) > ord(t[i]) :
            flg = False
    
    if flg and len(t) > len(s) :
        return 'Yes'
    else :
        return 'No'
    
print(solve())