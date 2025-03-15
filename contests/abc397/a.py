X = input()

a, b = map(int, X.split("."))


if a >= 38:
    print(1)
elif a == 37 and b >= 5:
    print(2)
else:
    print(3)
