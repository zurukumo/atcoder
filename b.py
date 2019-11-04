from collections import deque
N = int(input())
S = input()

mod = 10 ** 9 + 7

def solve() :
    if S[0] != 'B' or S[-1] != 'B' :
        return 0
        
    block = deque([])
    c = 1
    for i in range(1, 2 * N) :
        if S[i] == S[i-1] :
            c += 1
        else :
            block.append(c)
            c = 1
    block.append(c)
            
    ret = 1
    for i in range(1, N + 1) :
        ret *= i * i
        ret %= mod
    
    while len(block) > 1 :
        a = block.popleft()
        b = block.pop()
        if (a + b) % 2 != 0 :
            return 0
        ret *= pow((a + b) // 2, mod - 2, mod)
        ret %= mod
        
    return ret
        
print(solve())