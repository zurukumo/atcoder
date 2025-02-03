H, W, A, B = map(int, input().split())

ret = [['0'] * W for _ in range(H)]

A, B = B, A
for y in range(A) :
    for x in range(B, W) :
        ret[y][x] = '1'

for y in range(A, H) :
    for x in range(B) :
        ret[y][x] = '1'
        
for y in range(H) :
    print(''.join(ret[y]))