N = int(input())
a = [int(i) for i in input().split()]

ret = [0] * N

for i in range(N-1, -1, -1) :
    s = a[i]
    for j in range(i, N, i + 1) :
        s ^= ret[j]
    ret[i] = s
    
b = []
for i in range(N) :
    if ret[i] :
        b.append(i+1)

print(len(b))
print(' '.join([str(i) for i in b]))