N = int(input())
A = [int(i) for i in input().split()]

if A == sorted(A) and len(set(A)) == len(A):
    print("Yes")
else:
    print("No")
