A, B, C, D = map(int, input().split())

fr = max(A, C)
to = min(B, D)

if to - fr > 0 :
    print(to-fr)
else :
    print(0)