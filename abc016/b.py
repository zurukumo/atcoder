A, B, C = map(int, input().split())

is_plus = A + B == C
is_minus = A - B == C

if is_plus and is_minus:
    print("?")
elif is_plus:
    print("+")
elif is_minus:
    print("-")
else:
    print("!")
