b = [int(i) for i in input().split()]
N = int(input())
a = [int(input()) for _ in range(N)]

c = [0] * 10
for i in range(10) :
    c[b[i]] = i
    
def transform(x) :
    ret = 0
    base = 1
    while x :
        y = x % 10
        x //= 10
        ret += base * c[y]
        base *= 10
    return ret
    
d = []
for i in range(N) :
    d.append((transform(a[i]), a[i]))

d.sort()
for i in range(N) :
    print(d[i][1])