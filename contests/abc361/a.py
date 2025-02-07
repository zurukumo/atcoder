N, K, X = map(int, input().split())
A = [int(i) for i in input().split()]


print(*(A[:K] + [X] + A[K:]))
