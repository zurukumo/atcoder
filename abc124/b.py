N = int(input())
H = list(map(int, input().split()))

M = [0] * N
M[0] = 0

for i in range(1, N):
    M[i] = max(M[i - 1], H[i - 1])

ret = 0
for i in range(N):
    if H[i] >= M[i]:
        ret += 1

print(ret)
