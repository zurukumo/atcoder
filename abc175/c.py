X, K, D = map(int, input().split())

if X < 0:
    X = -X

if K * D < X:
    print(X - K * D)
else:
    K -= X // D
    X = X % D
    if K % 2 == 0:
        print(X)
    else:
        print(D - X)
