N = int(input())
d = [int(i) for i in input().split()]

ret = 0
for i in range(N):
    for j in range(i + 1, N):
        ret += d[i] * d[j]
print(ret)
