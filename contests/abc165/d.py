A, B, N = map(int, input().split())

N = min(N, B - 1)
print((A * N) // B - A * (N // B))
