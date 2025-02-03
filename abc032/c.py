N, K = map(int, input().split())
s = [int(input()) for _ in range(N)]

if 0 in s:
    print(N)
else:
    ret = 0
    mul = 1
    fr, to = 0, 0
    while to < N:
        if fr == to:
            mul *= s[to]
            to += 1
        elif mul > K:
            mul //= s[fr]
            fr += 1
        else:
            ret = max(ret, to - fr)
            mul *= s[to]
            to += 1
    if mul <= K:
        ret = max(ret, to - fr)

    print(ret)
