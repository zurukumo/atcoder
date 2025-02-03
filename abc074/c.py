A, B, C, D, E, F = map(int, input().split())

A *= 100
B *= 100

M = -float('inf')
Mwater, Msugar = 0, 0
for a in range(0, F + 1, A) :
    for b in range(0, F - a + 1, B) :
        for c in range(0, F - a - b + 1, C) :
            for d in range(0, F - a - b - c + 1, D) :
                if a + b + c + d == 0 :
                    continue
                if c + d <= (a + b) * E // 100 :
                    if 100 * (c + d) / (a + b + c + d) > M :
                        M = 100 * (c + d) / (a + b + c + d)
                        Mwater = a + b
                        Msugar = c + d
                        
print(Mwater+Msugar, Msugar)