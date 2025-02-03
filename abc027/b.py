N = int(input())
a = [int(i) for i in input().split()]

if sum(a) % N != 0 :
    print(-1)

else :
    avg = sum(a) // N

    ret = 0
    now = 0
    for i in range(N) :
        now += a[i]
        now -= avg

        if now != 0 :
            ret += 1

    print(ret)