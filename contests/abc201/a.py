A = sorted([int(i) for i in input().split()])

if A[2] - A[1] == A[1] - A[0]:
    print("Yes")
else:
    print("No")
