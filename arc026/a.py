N, A, B = map(int, input().split())

print(min(5, N) * B + max(0, N - 5) * A)
