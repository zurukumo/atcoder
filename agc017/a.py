N, P = map(int, input().split())
A = [int(i) for i in input().split()]

o, e = 0, 0
for i in range(N):
    if A[i] % 2 == 0:
        e += 1
    else:
        o += 1

ret = pow(2, e) * max(1, pow(2, o - 1))

if P == 0:
    print(ret)
else:
    print(pow(2, N) - ret)
