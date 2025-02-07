N, M = map(int, input().split())
X = [int(i) for i in input().split()]

ret = [0] * N

pre = X[0] - 1
for x in X[1:]:
    cur = x - 1
    l = min(pre, cur)
    r = max(pre, cur)
    ret[0] += r - l
    ret[l] -= r - l
    ret[l] += N - (r - l)
    ret[r] -= N - (r - l)
    ret[r] += r - l
    pre = cur

for i in range(1, N):
    ret[i] += ret[i - 1]


print(min(ret))
