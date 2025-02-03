N, K = map(int, input().split())

ret = 0
if K == 0 :
    ret = N * N
else :
    for a in range(1, N + 1) :
        ret += (N // a) * max(0, a - K)
        ret += max(0, N % a - K + 1)
print(ret)