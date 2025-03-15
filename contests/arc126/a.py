T = int(input())
for _ in range(T):
    N2, N3, N4 = map(int, input().split())

    ret = 0

    x = min(N3 // 2, N4)
    ret += x
    N3 -= x * 2
    N4 -= x

    x = min(N3 // 2, N2 // 2)
    ret += x
    N3 -= x * 2
    N2 -= x * 2

    x = min(N4 // 2, N2)
    ret += x
    N4 -= x * 2
    N2 -= x

    x = min(N4, N2 // 3)
    ret += x
    N4 -= x
    N2 -= x * 3

    x = N2 // 5
    ret += x
    N2 -= x * 5

    print(ret)
