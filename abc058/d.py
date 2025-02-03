n, m = map(int, input().split())

x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

MOD = 10 ** 9 + 7

sx = 0
pre = 0
for i in range(1, n) :
    pre += (x[i]-x[i-1]) * i
    sx += pre
    sx %= MOD
    
sy = 0
pre = 0
for i in range(1, m) :
    pre += (y[i]-y[i-1]) * i
    sy += pre
    sy %= MOD
    
print(sx*sy%MOD)