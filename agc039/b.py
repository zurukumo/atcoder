S = list(input())
K = int(input())

S = S + S + S
N = len(S)

a = 0
b = 0
c = 0
for i in range(1, N) : 
    if S[i] == S[i-1] :
        if i < N // 3 :
            a += 1
        elif i < N // 3 * 2 :
            b += 1
        else :
            c += 1
        S[i] = '#'
        
ret = a + K // 2 * b + (K - K // 2 - 1) * c
print(ret)