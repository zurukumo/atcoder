import sys
input = sys.stdin.readline

N, W = map(int, input().split())
wv = [[int(i) for i in input().split()] for _ in range(N)]

s = [[] for _ in range(4)]
w0 = wv[0][0]
for w, v in wv :
    s[w-w0].append(v)
for i in range(4) :
    s[i].sort(reverse=True)
    s[i] = [0] + s[i]
    for j in range(1, len(s[i])) :
        s[i][j] += s[i][j-1]

M = 0
for i0 in range(len(s[0])) :
    for i1 in range(len(s[1])) :
        for i2 in range(len(s[2])) :
            for i3 in range(len(s[3])) :
                if i0*w0+i1*(w0+1)+i2*(w0+2)+i3*(w0+3) <= W :
                    M = max(M, s[0][i0]+s[1][i1]+s[2][i2]+s[3][i3])
                    
print(M)