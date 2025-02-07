N = int(input())
A = [int(i) for i in input().split()]

print(*(A[i] * A[i + 1] for i in range(N - 1)))
