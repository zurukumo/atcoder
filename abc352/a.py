N, X, Y, Z = map(int, input().split())

X, Y = min(X, Y), max(X, Y)
if X < Z < Y:
    print("Yes")
else:
    print("No")
