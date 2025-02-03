N, Y = map(int, input().split())

def solve() :
    for i in range(N + 1) :
        for j in range(N + 1 - i) :
            k = N - i - j
            if i * 10000 + j * 5000 + k * 1000 == Y :
                return (i, j, k)
    return (-1, -1, -1)
    
print(*solve())