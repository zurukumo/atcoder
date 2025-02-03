c = [[int(i) for i in input().split()] for _ in range(3)]

h1 = c[1][0] - c[0][0] == c[1][1] - c[0][1] == c[1][2] - c[0][2]
h2 = c[2][0] - c[1][0] == c[2][1] - c[1][1] == c[2][2] - c[1][2]
w1 = c[0][1] - c[0][0] == c[1][1] - c[1][0] == c[2][1] - c[2][0]
w2 = c[0][2] - c[0][1] == c[1][2] - c[1][1] == c[2][2] - c[2][1]

if h1 and h2 and w1 and w2 :
    print('Yes')
else :
    print('No')