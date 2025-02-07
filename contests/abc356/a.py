N, L, R = map(int, input().split())
ret = list(range(1, L)) + list(range(R, L - 1, -1)) + list(range(R + 1, N + 1))
print(*ret)
