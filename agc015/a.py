N, A, B = map(int, input().split())

if N == 1:
    if A == B:
        print(1)
    else:
        print(0)

elif A <= B:
    print((B - A) * (N - 2) + 1)

else:
    print(0)
