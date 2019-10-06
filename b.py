N, K = map(int, input().split())
h = [int(i) for i in input().split()]

ret = 0
for i in range(N) :
    if h[i] >= K :
        ret += 1
print(ret)