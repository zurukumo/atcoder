V, A, B, C = map(int, input().split())

V %= A + B + C
if 0 <= V < A:
    print("F")
elif A <= V < A + B:
    print("M")
else:
    print("T")
