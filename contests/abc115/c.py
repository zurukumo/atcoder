N, K = map(int, input().split())
h = [int(input()) for _ in range(N)]

h.sort()

ret = float("inf")
for i in range(N - K + 1):
    ret = min(ret, h[i + K - 1] - h[i])
print(ret)
