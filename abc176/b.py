N = input()

s = 0
for n in N:
    s += int(n)
    s %= 9
if s == 0:
    print("Yes")
else:
    print("No")
