N = int(input())
A = [int(i) for i in input().split()]

A[A.index(max(A))] = -float("inf")
print(A.index(max(A)) + 1)
