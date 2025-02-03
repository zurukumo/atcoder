from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
st = [[int(i) for i in input().split()] for _ in range(M)]

imos = [0] * (N + 2)

for s, t in st:
    imos[s] += 1
    imos[t + 1] -= 1

for i in range(1, N + 2):
    imos[i] += imos[i - 1]

less = []
for i in range(N + 2):
    if imos[i] <= 1:
        less.append(i)

ret = []
for i, (s, t) in enumerate(st):
    if less[bisect_right(less, t) - 1] < s:
        ret.append(i + 1)

print(len(ret))
for r in ret:
    print(r)
