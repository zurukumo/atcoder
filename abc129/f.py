L, A, B, M = map(int, input().split())

def mat_pow(x, n) :
    y = [[0] * 3 for _ in range(3)]
        
    for i in range(3) :
        y[i][i] = 1
        
    while n > 0 :
        if n & 1 :
            y = mat_mul(x, y)
        x = mat_mul(x, x)
        n >>= 1
        
    return y
    
def mat_mul(a, b) :
    I, J, K = len(a), len(b[0]), len(b)
    c = [[0] * J for _ in range(I)]
    for i in range(I) :
        for j in range(J) :
            for k in range(K) :
                c[i][j] += a[i][k] * b[k][j]
            c[i][j] %= M
    return c

n0 = -(-(10 ** 0 - A) // B)
n1 = -(-(10 ** 1 - A) // B)

ret = [[0], [A], [1]]

for d in range(1, 19) :
    mat = [[10**d, 1, 0], [0, 1, B], [0, 0, 1]]
    if n0 < 0 and 0 < n1 :
        n0 = 0
        
    if 0 <= n0 < n1 :
        ret = mat_mul(mat_pow(mat, n1 - n0), ret)
    n0, n1 = n1, min(-(-(10 ** (d + 1) - A) // B), L)

print(ret[0][0])