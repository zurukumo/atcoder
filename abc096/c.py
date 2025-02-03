H, W = map(int, input().split())
s = [input() for _ in range(H)]

def check() :
    for y in range(H) :
        for x in range(W) :
            if s[y][x] == '.' :
                continue
                
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
                if not (0 <= (y + dy) < H and 0 <= (x + dx) < W) :
                    continue
                if s[y+dy][x+dx] == '#' :
                    break
            else :
                return 'No'
    return 'Yes'
    
print(check())