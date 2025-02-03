import heapq

N, M = map(int, input().split())
P = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]
D = [int(i) for i in input().split()]

P.sort(reverse=True)
LD = []
for l, d in zip(L, D):
    LD.append((l, d))
LD.sort(reverse=True)

ret = 0
queue = []
while P:
    p = P.pop()

    # pより安いものをqueueに追加する
    while LD and LD[-1][0] <= p:
        l, d = LD.pop()
        heapq.heappush(queue, -d)

    ret += p
    if queue:
        d = heapq.heappop(queue)
        ret += d


print(ret)
