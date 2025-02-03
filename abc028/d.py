N, K = map(int, input().split())

ret = 0

# 3つともK
ret += 1

# 2つK
ret += 3 * (N - 1)

# 1つK
ret += 6 * (K - 1) * (N - K)

print(ret / (N**3))
