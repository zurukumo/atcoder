N = int(input())
A = [int(i) for i in input().split()]

print(max(a for a in A if a != max(A)))
