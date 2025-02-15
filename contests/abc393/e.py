N, K = map(int, input().split())
A = [int(i) for i in input().split()]

s = [0] * (10**6 + 1)
ret = [1] * (10**6 + 1)
for a in A:
    s[a] += 1

for i in range(1, 10**6 + 1):
    c = 0
    j = i
    while j <= 10**6:
        c += s[j]
        j += i
    if c >= K:
        j = i
        while j <= 10**6:
            ret[j] = i
            j += i

for a in A:
    print(ret[a])
