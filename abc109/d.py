H, W = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(H)]

op = []
for y in range(H - 1) :
    for x in range(W) :
        if a[y][x] % 2 != 0 :
            op.append((y + 1, x + 1, y + 2, x + 1))
            a[y+1][x] += 1

for x in range(W - 1) :
    if a[H-1][x] % 2 != 0 :
        op.append((H, x + 1, H, x + 2))
        a[H-1][x+1] += 1
        
print(len(op))
for op_ in op :
    print(*op_)