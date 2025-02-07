N = int(input())
A = [int(i) for i in input().split()]

if len(set(A)) == 1:
    print("Yes")
else:
    print("No")
