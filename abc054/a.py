A, B = map(int, input().split())

A = (A + 12) % 14
B = (B + 12) % 14

if A > B:
    print("Alice")
elif A == B:
    print("Draw")
else:
    print("Bob")
