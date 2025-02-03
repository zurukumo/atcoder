ABCDE = [int(input()) for _ in range(5)]
ABCDE_ = [(ABCDE[i] + 9) // 10 * 10 for i in range(5)]

s = sum(ABCDE_)
m = float('inf')
for i in range(5) :
    m = min(m, s - (ABCDE_[i] - ABCDE[i]))
    
print(m)