from collections import defaultdict

N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]

cnt = defaultdict(int)
for a, b in ab :
    if a > b :
        a, b = b, a
        
    if a == 1 :
        cnt[(a, b)] += 1
    else :
        cnt[(1, a)] += 1
        cnt[(1, b)] += 1
        
flag = True
for i in cnt.values() :
    if i % 2 == 1 :
        flag = False
        
if flag :
    print('YES')
else :
    print('NO')