N, T = map(int, input().split())
t = [int(i) for i in input().split()]

ret = 0
cur = 0
for tt in t :
    if tt < cur :
        ret += tt + T - cur
    else :
        ret += T
    cur = tt + T
    
print(ret)