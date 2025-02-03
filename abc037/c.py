N, K = map(int, input().split())
a = [int(i) for i in input().split()]

s = [0] * (N + 1)
for i in range(N) :
    s[i+1] += s[i] + a[i]

ret = 0
for i in range(K, N + 1) :
    ret += s[i] - s[i-K]

print(ret)