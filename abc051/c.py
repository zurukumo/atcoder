sx, sy, tx, ty = map(int, input().split())

dx, dy = tx-sx, ty-sy
u = 'U'*dy+'R'*dx+'D'*dy+'L'*(dx+1)+'U'*(dy+1)+'R'*(dx+1)+'DR'+'D'*(dy+1)+'L'*(dx+1)+'U'

print(u)
