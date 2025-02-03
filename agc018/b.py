from collections import Counter

N, M = map(int, input().split())
A = [[int(i) for i in input().split()] for _ in range(N)]

for i in range(N) :
    A[i] = A[i][::-1]

def solve() :
    ret = float('inf')
    select = [True] * (M + 1)

    while True :
        c = Counter([A[i][-1] for i in range(N)])
        for k, v in c.items() :
            if v >= ret :
                select[k] = False
                
        ret = min(ret, max(c.values()))
        
        for i in range(N) :
            while not select[A[i][-1]] :
                A[i].pop()
                if len(A[i]) == 0 :
                    return ret
                    
print(solve())
                