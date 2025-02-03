N = int(input())
A = [0] + [int(i) for i in input().split()] + [0]

s = 0
for i in range(1, N + 2):
    s += abs(A[i] - A[i - 1])

for i in range(1, N + 1):
    if min(A[i - 1], A[i + 1]) <= A[i] <= max(A[i - 1], A[i + 1]):
        print(s)
    else:
        print(
            s - abs(A[i] - A[i - 1]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1])
        )
