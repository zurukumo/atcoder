N = int(input())
A = [int(i) for i in input().split()]
MOD = 10 ** 9 + 7

def judge() :
    p = N % 2
    c = [0] * ((N + 1) // 2)

    for a in A :
        if a % 2 == p or a < 0 or N <= a :
            return 0
            
        c[a//2] += 1
 
    if p == 1 and c[0] == 1 and c[1:].count(2) == (N - 1) // 2 :
        return pow(2, (N - 1) // 2, MOD)
    
    elif p == 0 and c.count(2) == N // 2 :
        return pow(2, N // 2, MOD)
        
    return 0
    
print(judge())