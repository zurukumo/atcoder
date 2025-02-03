A, B, C, D = map(int, input().split())

def gcd(m, n) :
    r = m % n
    while r != 0 :
        m, n = n, r
        r = m % n
    return n

CD = (C * D) // gcd(C, D)

C1 = (A - 1) // C
C2 = B // C
D1 = (A - 1) // D
D2 = B // D
CD1 = (A - 1) // CD
CD2 = B // CD

print(B - A + 1 - (C2 - C1 + D2 - D1 - (CD2 - CD1)))