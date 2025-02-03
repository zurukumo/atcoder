N, M, K = map(int, input().split())
A = [int(i) for i in input().split()]


i = 2**31
ret = 0
while i > 0:
    new_ret = ret | i
    B = []
    for a in A:
        for j in range(32, -1, -1):
            if (new_ret & (1 << j)) and not (a & (1 << j)):
                B.append((new_ret % (2 ** (j + 1))) - (a % (2 ** (j + 1))))
                break
        else:
            B.append(0)
    B.sort()
    if sum(B[:K]) <= M:
        ret = new_ret
    i >>= 1

print(ret)
