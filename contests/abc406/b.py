N, K = map(int, input().split())
A = [int(i) for i in input().split()]

ret = 1
for a in A:
    ret *= a
    if ret >= 10**K:
        ret = 1

print(ret)
