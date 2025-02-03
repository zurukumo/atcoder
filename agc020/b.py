K = int(input())
A = [int(i) for i in input().split()]

def solve() :            
    m, M = 2, 2
    for a in A[::-1] :
        if (m - 1) // a == M // a :
            return [-1]
            
        M = M // a * a + a - 1
        x = (m + a - 1) // a
        m = a * x
        
    return [m, M]
    
print(*solve())