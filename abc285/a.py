a, b = map(int, input().split())

a, b = min(a, b), max(a, b)
if b == a * 2 or b == a * 2 + 1:
    print("Yes")
else:
    print("No")
