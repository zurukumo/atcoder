N = int(input())
A = [int(input()) for _ in range(N)]

B = sorted(A)
M1 = B[-1]
M2 = B[-2]

for a in A :
    if a == M1 :
        print(M2)
    else :
        print(M1)
