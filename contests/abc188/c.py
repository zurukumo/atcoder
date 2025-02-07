N = int(input())
A = [int(i) for i in input().split()]

w = min(max(A[: 2 ** (N - 1)]), max(A[2 ** (N - 1) :]))
print(A.index(w) + 1)
