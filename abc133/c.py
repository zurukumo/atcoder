L, R = map(int, input().split())
MOD = 2019

m = float('inf')
if L + MOD < R :
    for i in range(MOD) :
        for j in range(MOD) :
            m = min(m, i*j%MOD)
else :
    for i in range(L, R) :
        for j in range(i+1, R+1) :
            m = min(m, i*j%MOD)
            
print(m)