N, C = map(int, input().split())
xv = [[int(i) for i in input().split()] for _ in range(N)]

l1 = [xv[i][1] for i in range(N)]
l2 = l1[::]
r1 = l1[::-1]
r2 = r1[::]

for i in range(1, N) :
    l1[i] += l1[i-1]
    l2[i] += l2[i-1]
    r1[i] += r1[i-1]
    r2[i] += r2[i-1]
    
for i in range(N) :
    x = xv[i][0]
    l1[i] -= x
    l2[i] -= 2 * x
    r1[N-1-i] -= C - x
    r2[N-1-i] -= 2 * (C - x)

for i in range(1, N) :
    l1[i] = max(l1[i], l1[i-1])
    r1[i] = max(r1[i], r1[i-1])

ret = max(l1[-1], r1[-1])
for i in range(N-1) :
    ret = max(ret, l2[i] + r1[N-2-i])
    ret = max(ret, r2[i] + l1[N-2-i])
    
print(max(ret, 0))