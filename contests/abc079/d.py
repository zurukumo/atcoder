H, W = map(int, input().split())
c = [[int(i) for i in input().split()] for _ in range(10)]
A = [[int(i) for i in input().split()] for _ in range(H)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

count = [0] * 10
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            count[A[i][j]] += 1

ret = 0
for i in range(10):
    ret += count[i] * c[i][1]
print(ret)
