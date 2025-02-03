N, x = map(int, input().split())
a = [int(i) for i in input().split()]

ret = 0
for i in range(N - 1):
    if a[i] + a[i + 1] > x:
        ret += a[i] + a[i + 1] - x

        if a[i] >= x:
            a[i] = x
            a[i + 1] = 0
        else:
            a[i + 1] = x - a[i]

print(ret)
