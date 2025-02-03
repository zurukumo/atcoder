N = int(input())
K = int(input())
x = [int(i) for i in input().split()]

ret = 0
for xx in x:
    if xx < K - xx:
        ret += 2 * xx
    else:
        ret += 2 * (K - xx)

print(ret)
