X = input()

a, b = X.split(".")
if int(b[0]) < 5:
    print(int(a))
else:
    print(int(a) + 1)
