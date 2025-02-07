N = int(input())
A = [int(i) for i in input().split()]

o = 0
for a in A:
    if a % 2 == 1:
        o += 1

if o % 2 != 0:
    print("NO")
else:
    print("YES")
