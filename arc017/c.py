from collections import defaultdict

N, X = map(int, input().split())
w = [int(input()) for _ in range(N)]

half = N // 2

a = defaultdict(int)
a[0] = 1
for i in range(half) :
    keys, values = list(a.keys()), list(a.values())
    for k, v in zip(keys, values) :
        a[k+w[i]] += v
    
b = defaultdict(int)
b[0] = 1
for i in range(half, N) :
    keys, values = list(b.keys()), list(b.values())
    for k, v in zip(keys, values) :
        b[k+w[i]] += v

ret = 0
for k, v in a.items() :
    ret += v * b[X - k]

print(ret)