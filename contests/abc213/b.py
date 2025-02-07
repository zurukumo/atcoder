N = int(input())
A = [int(i) for i in input().split()]
B = sorted(A)

booby = B[-2]
print(A.index(booby) + 1)
