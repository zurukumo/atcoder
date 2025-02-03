A = [list(input()) for _ in range(10)]

def search(y, x, c) :
    q = [(y, x)]
    visited[y][x] = c
    while q :
        cy, cx = q.pop()        
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
            ny, nx = cy + dy, cx + dx
            if 0 <= nx < 10 and 0 <= ny < 10 and A[ny][nx] == 'o' and visited[ny][nx] == -1 :
                visited[ny][nx] = c
                q.append((ny, nx))
            
visited = [[-1] * 10 for _ in range(10)]
c = 0
for y in range(10) :
    for x in range(10) :
        if A[y][x] == 'o' and visited[y][x] == -1 :
            search(y, x, c)
            c += 1

def judge() : 
    for y in range(10) :
        for x in range(10) :
            if visited[y][x] != -1 : continue
            s = set()
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)) :
                ny, nx = y + dy, x + dx
                if 0 <= nx < 10 and 0 <= ny < 10 and visited[ny][nx] >= 0 :
                    s.add(visited[ny][nx])
            if len(s) == c :
                return 'YES'
                
    return 'NO'
    
print(judge())