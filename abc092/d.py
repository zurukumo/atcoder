A, B = map(int, input().split())
A -= 1
B -= 1

ret = [[i // 50] * 100 for i in range(100)]

x, y = 0, 0
while A :
    ret[y][x] = 1
    A -= 1
    x += 2
    if x >= 100 :
        x = 0
        y += 2
        
x, y = 0, 51
while B :
    ret[y][x] = 0
    B -= 1
    x += 2
    if x >= 100 :
        x = 0
        y += 2
        
print(100, 100)
for y in range(100) :
    print(''.join(['#' if ret[y][x] == 0 else '.' for x in range(100)]))