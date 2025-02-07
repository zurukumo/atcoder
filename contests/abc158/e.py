from collections import defaultdict

N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ret = 0
    for i, v in enumerate(S):
        if int(v) % P == 0:
            ret += i + 1
    print(ret)

else:
    mem = defaultdict(int)
    mem[0] += 1

    T = [0]
    dec = 1
    x = 0
    for s in S[::-1]:
        s = int(s)
        x = (dec * s + x) % P
        dec = dec * 10 % P
        T.append(x)
        mem[x] += 1

    ret = 0
    for i, t in enumerate(T):
        ret += mem[t] - 1
        mem[t] -= 1

    print(ret)
