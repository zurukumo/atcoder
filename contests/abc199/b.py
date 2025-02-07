N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

M = max(A)
m = min(B)
print(max(0, m - M + 1))
