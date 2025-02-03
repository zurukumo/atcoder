N, K = map(int, input().split())
a = [int(i) for i in input().split()]

s = [0] + a[::]
t = [0] + [a[i] if a[i] > 0 else 0 for i in range(N)]

for i in range(1, N + 1) :
    s[i] += s[i-1]
    t[i] += t[i-1]

ret = -float('inf')
for i in range(1, N - K + 2) :
    ret = max(ret, t[N] - t[i+K-1] + t[i-1] + max(0, s[i+K-1] - s[i-1]))
print(ret)