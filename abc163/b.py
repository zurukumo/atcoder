N, M = map(int, input().split())
A = [int(i) for i in input().split()]

ret = N - sum(A)
if ret < 0:
    print(-1)
else:
    print(ret)
