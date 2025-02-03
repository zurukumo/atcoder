N, X = map(int, input().split())
VP = [[int(i) for i in input().split()] for _ in range(N)]

# Σ (V * P / 100) > X
# Σ (V * P) > X * 100

s = 0
for i, (V, P) in enumerate(VP):
    s += V * P
    if s > X * 100:
        print(i + 1)
        break
else:
    print(-1)
