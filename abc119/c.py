N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

ret = float('inf')

def mp(x, target) :
    ret = -10
    long = 0
    for i in range(N) :
        if x & 1 :
            ret += 10
            long += l[i]
        x >>= 1
    ret += abs(long - target)
    return ret

for i in range(1, 1 << N) :
    for j in range(1, 1 << N) :
        if i & j :
            continue
        for k in range(1, 1 << N) :
            if i & k or j & k :
                continue
            ret = min(ret, mp(i, A) + mp(j, B) + mp(k, C))

print(ret)