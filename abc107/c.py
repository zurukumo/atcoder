N, K = map(int, input().split())
x = [int(i) for i in input().split()]

ret = float('inf')
for i in range(N-K+1) :
    l = x[i]
    r = x[i+K-1]
    if l < 0 and r < 0 :
        ret = min(ret, -l)
    elif l > 0 and r > 0 :
        ret = min(ret, r)
    else :
        m, M = min(-l, r), max(-l, r)
        ret = min(ret, m * 2 + M)
print(ret)