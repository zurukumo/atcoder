A, B, C = map(int, input().split())

if C == 0:
    if A <= B:
        print("Aoki")
    else:
        print("Takahashi")
else:
    if B <= A:
        print("Takahashi")
    else:
        print("Aoki")
