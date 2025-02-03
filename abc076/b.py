N = int(input())
K = int(input())

m = float('inf')
for i in range(N + 1) :
    m = min(m, 2 ** i + (N - i) * K)
print(m)