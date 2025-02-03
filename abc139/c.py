N = int(input())
H = [int(i) for i in input().split()] + [float("inf")]
now = 0
ret = 0
for i in range(1, N + 1):
    if H[i] <= H[i - 1]:
        now += 1
    else:
        ret = max(ret, now)
        now = 0
print(ret)
