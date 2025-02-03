A, B, C = map(int, input().split())

if A == 7 and B == C == 5:
    print("YES")
elif B == 7 and A == C == 5:
    print("YES")
elif C == 7 and A == B == 5:
    print("YES")
else:
    print("NO")
