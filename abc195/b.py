A, B, W = map(int, input().split())

W *= 1000

m = float('inf')
M = -float('inf')
for i in range(10 ** 6 + 10):
    if A * i > W:
        break
    if A * i <= W <= B * i:
        m = min(m, i)
        M = max(M, i)


if m == float('inf'):
    print('UNSATISFIABLE')
else:
    print(m, M)
