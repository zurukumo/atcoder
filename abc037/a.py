A, B, C = map(int, input().split())

if A > B :
    A, B = B, A
    
print(C // A)