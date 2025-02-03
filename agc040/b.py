N = int(input())
LR = [[int(i) for i in input().split()] for _ in range(N)]

for i in range(N) :
    LR[i][1] += 1

a, b = 0, 0
la, ra = 0, float('inf')
lb, rb = -float('inf'), 0

for i, (l, r) in enumerate(LR) :
    if r < ra or (r == ra and l < la) :
        la, ra = l, r
        a = i
        
    if l > lb or (l == rb and r > rb) :
        lb, rb = l, r
        b = i

ret = 0

Md = 0
for i, (l, r) in enumerate(LR) :
    if i != a and i != b :
        Md = max(Md, r - l)
ret = max(ret, max(0, ra - lb) + Md)

LR.sort(key=lambda x: x[1])
LR.sort()
dpl = [0] * N
dpr = [0] * N

dpl[0] = max(la, LR[0][0])
dpr[N-1] = min(rb, LR[N-1][1])

for i in range(1, N) :
    dpl[i] = max(dpl[i-1], LR[i][0])
    dpr[N-1-i] = min(dpr[N-i], LR[N-1-i][1])
    
for i in range(N - 1) :
    ret = max(ret, max(0, ra - dpl[i]) + max(0, dpr[i + 1] - lb))
    
print(ret)