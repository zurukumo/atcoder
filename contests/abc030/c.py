from bisect import bisect

N, M = map(int, input().split())
X, Y = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

cur = -Y
ret = 0
while True:
    nex = bisect(a, cur + Y - 1)
    if nex >= N:
        break
    cur = a[nex]

    nex = bisect(b, cur + X - 1)
    if nex >= M:
        break
    cur = b[nex]
    ret += 1

print(ret)
