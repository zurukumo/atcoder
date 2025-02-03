from bisect import bisect_left

s = input()
t = input()
ls, lt = len(s), len(t)

exsist = [[] for _ in range(26)]
for i in range(ls) :
    exsist[ord(s[i])-97].append(i)

ret = 0
now = -1
for i in range(lt) :
    ot = ord(t[i])-97
    if len(exsist[ot]) == 0 :
        print('-1')
        break
    
    a = bisect_left(exsist[ot], now + 1)
    if a == len(exsist[ot]) :
        ret += ls
        now = exsist[ot][bisect_left(exsist[ot], -1)]
    else :
        now = exsist[ot][a]
        
else :
    print(ret+now+1)