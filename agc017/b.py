N, A, B, C, D = map(int, input().split())

def solve() :
    if N % 2 == 0 :
        l = (N // 2) * C - (N // 2) * D
        r = (N // 2) * D - (N // 2) * C
        for _ in range(N // 2 + 1) :
            if A + l <= B <= A + r :
                return 'YES'
            if A - r <= B <= A - l :
                return 'YES'
            l += C + D
            r += C + D
            
    else :
        l = (N // 2 + 1) * C - (N // 2) * D
        r = (N // 2 + 1) * D - (N // 2) * C
        for _ in range(N // 2 + 1) :
            if A + l <= B <= A + r :
                return 'YES'
            if A - r <= B <= A - l :
                return 'YES'
            l += C + D
            r += C + D
            
    return 'NO'
    
N -= 1    
print(solve())