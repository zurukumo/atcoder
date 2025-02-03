K = int(input())
X, Y = map(int, input().split())

swap = False
if abs(X) < abs(Y) :
    swap = True
    X, Y = Y, X
    
signX, signY = 1, 1
if X < 0 : 
    signX = -1
    X = -X
if Y < 0 :
    signY = -1
    Y = -Y

def output(x, y) :
    if swap :
        print(y*signY, x*signX)
    else :
        print(x*signX, y*signY)

if K % 2 == 0 and (X + Y) % 2 == 1 :
    print(-1)
else :
    if K > X + Y and (X + Y) % 2 == 1 :
        print(3)
        output(X, -(K - X))
        output(X + (K + X - Y) // 2, -(K - X) + (K - X + Y) // 2)
        output(X, Y)
    else :
        if K > X + Y and (X + Y) % 2 == 0 :
            n = 2
        else :
            n = (X + Y + K - 1) // K
            if (X + Y) % 2 != n * K % 2 :
                n += 1
        print(n)
        a = (K*n-X-Y)//2//K
        b = (K*n+X-Y)//2//K
        x0 = K*(a+1)-(K*n-X-Y)//2
        y0 = K*(b+1)-X-(K*n-X-Y)
        for i in range(a) :
            output(0, -(i+1)*K)
        for i in range(b-a) :
            output(x0+i*K, -(K*n-X-Y)//2)
        for i in range(n-b) :
            output(X, y0 + i*K)