X, Y, Z, K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

s = []
for x in range(X) :
    for y in range(Y) :
        s.append(A[x]+B[y])
s.sort(reverse=True)

t = []
for k in range(min(K, len(s))) :
    for z in range(Z) :
        t.append(s[k]+C[z])
        
t.sort(reverse=True)

print("\n".join(map(str, t[:K])))