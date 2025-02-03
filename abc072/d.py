N = int(input())
p = [int(i) for i in input().split()]

ret = 0
for i in range(N-1) :
    if p[i] == i + 1 :
        p[i], p[i+1] = p[i+1], p[i]
        ret += 1
if p[N-1] == N :
    ret += 1
    
print(ret)