n = int(input())

ret = float('inf')
for h in range(1, n + 1) :
    w = n // h
    m = n - h * w
    ret = min(ret, abs(h-w) + m)
    
print(ret)