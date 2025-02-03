R, C = [int(i) for i in input().split()]
sx, sy = [int(i)-1 for i in input().split()]
gx, gy = [int(i)-1 for i in input().split()]
c = [input() for _ in range(R)]

q = [[sx, sy]]
path = [[R*C for _ in range(C)] for _ in range(R)]
path[sx][sy] = 0

while len(q) > 0 :
	x, y = q.pop(0)
	current = path[x][y] + 1
	
	if c[x][y-1] == '.' and current < path[x][y-1] :
		q.append([x, y-1])
		path[x][y-1] = current
	if c[x][y+1] == '.' and current < path[x][y+1] :
		q.append([x, y+1])
		path[x][y+1] = current
	if c[x-1][y] == '.' and current < path[x-1][y] :
		q.append([x-1, y])
		path[x-1][y] = current
	if c[x+1][y] == '.' and current < path[x+1][y] :
		q.append([x+1, y])
		path[x+1][y] = current
		
print(path[gx][gy])