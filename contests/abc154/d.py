N, K = map(int, input().split())
p = [int(i) for i in input().split()]

for i in range(N):
    p[i] = p[i] * (p[i] + 1) // 2 / p[i]

p = [0] + p

for i in range(1, N + 1):
    p[i] += p[i - 1]

ret = 0
for i in range(K, N + 1):
    ret = max(ret, p[i] - p[i - K])

print(ret)
