N, K = map(int, input().split())
h = [int(i) for i in input().split()]

ret = 0
for hi in h:
    if hi >= K:
        ret += 1

print(ret)
