a, b = map(int, input().split())

if b < 0 and a % 2 == b % 2:
    print("Negative")
elif a <= 0 <= b:
    print("Zero")
else:
    print("Positive")
