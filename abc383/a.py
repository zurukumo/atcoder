N = int(input())
TV = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
pre = 0
for t, v in TV:
    ret = max(0, ret - (t - pre))
    ret += v
    pre = t

# print(ret)
