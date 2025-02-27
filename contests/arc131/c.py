N = int(input())
A = [int(i) for i in input().split()]


s = 0
for a in A:
    s ^= a

if s in A:
    print("Win")
else:
    if N % 2 == 0:
        print("Lose")
    else:
        print("Win")
