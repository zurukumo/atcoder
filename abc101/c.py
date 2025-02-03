N, K = map(int, input().split())
A = [int(i) for i in input().split()]

print((N - K + K - 2) // (K - 1) + 1)