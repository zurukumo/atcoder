N = int(input())
a = [int(i) for i in input().split()]

x, y, z = 0, 0, 0
for i in range(N):
    if a[i] % 4 == 0:
        x += 1
    elif a[i] % 2 == 0:
        y += 1
    else:
        z += 1

if y > 0:
    z += 1

if z <= x + 1:
    print("Yes")
else:
    print("No")
