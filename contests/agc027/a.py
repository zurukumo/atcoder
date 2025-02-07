N, x = map(int, input().split())
a = [int(i) for i in input().split()]

if sum(a) == x:
    print(N)
else:
    a.sort()
    s = 0
    for i in range(N):
        if s + a[i] > x:
            break
        s += a[i]

    print(i)
