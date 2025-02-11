A1, A2, A3 = map(int, input().split())

A1, A2, A3 = sorted([A1, A2, A3])
if A1 * A2 == A3:
    print("Yes")
else:
    print("No")
