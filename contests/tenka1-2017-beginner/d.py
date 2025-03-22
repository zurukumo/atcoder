N, K = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for A, B in AB:
    if A & ~K == 0:
        ret += B

for i in range(30):
    if K & (1 << i) == 0:
        continue

    k = K
    k ^= 1 << i
    k |= (1 << i) - 1
    s = 0
    for A, B in AB:
        if A & ~k == 0:
            s += B

    ret = max(ret, s)

print(ret)
