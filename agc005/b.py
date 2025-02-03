from heapq import heappush, heappop

N = int(input())
a = [int(i) for i in input().split()]

b = [N] * N
c = [-1] * N

h = []
for i in range(N) :
    while len(h) > 0 and -h[0][0] > a[i] :
        b[h[0][1]] = i
        heappop(h)
    heappush(h, (-a[i], i))

h = []
for i in range(N - 1, -1, -1) :
    while len(h) > 0 and -h[0][0] > a[i] :
        c[h[0][1]] = i
        heappop(h)
    heappush(h, (-a[i], i))

ret = 0
for i in range(N) :
    ret += a[i] * (b[i] - i) * (i - c[i])
print(ret)