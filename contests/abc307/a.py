N = int(input())
A = [int(i) for i in input().split()]

print(*(sum(A[7 * i : 7 * (i + 1)]) for i in range(N)))
