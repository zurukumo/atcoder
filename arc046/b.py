N = int(input())
A, B = map(int, input().split())

if A == B :
    if N // (A + 1) * (A + 1) != N :
        print('Takahashi')
    else :
        print('Aoki')
elif A > B :
    print('Takahashi')
else :
    if N <= A :
        print('Takahashi')
    else :
        print('Aoki')