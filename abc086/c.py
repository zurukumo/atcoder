N = int(input())
txy = [[int(i) for i in input().split()] for _ in range(N)]

def solve() :
    pt, px, py = 0, 0, 0
    for t, x, y in txy :
        dd = abs(x-px) + abs(y-py)
        dt = t - pt
        if dd > dt or dd % 2 != dt % 2 :
            return 'No'
            
        pt, px, py = t, x, y
        
    return 'Yes'
    
print(solve())