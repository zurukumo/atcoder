N, K = map(int, input().split())
A = [int(i) for i in input().split()]

def gcd(a, b) :
    if b > a : 
        a, b = b, a
    
    while b != 0 :
        a, b = b, a % b
    return a

def solve() :
    x = A[0]

    for a in A[1:] :
        x = gcd(x, a)
        
    for a in A :
        if a >= K and (a - K) % x == 0 :
            return 'POSSIBLE'
            
    return 'IMPOSSIBLE'
    
print(solve())