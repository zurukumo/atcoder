A, B, C, D = map(int, input().split())

if A * 60 + B < C * 60 + D + 1:
    print("Takahashi")
else:
    print("Aoki")
