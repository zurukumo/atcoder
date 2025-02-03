N, T = map(int, input().split())
A = [int(i) for i in input().split()]

m = [A[0]]

mv = A[0]
for a in A[1:] :
    if a < mv :
        m.append(a)
        mv = a
    else :
        m.append(mv)

Md, Mn = 0, 0
for i in range(N - 1, 0, -1) :
    d = A[i] - m[i-1]
    if d > Md :
        Md, Mn = d, 1
    elif d == Md :
        Mn += 1
        
print(Mn)