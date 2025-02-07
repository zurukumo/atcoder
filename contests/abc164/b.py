from math import ceil

A, B, C, D = map(int, input().split())

if ceil(C / B) <= ceil(A / D):
    print("Yes")
else:
    print("No")
