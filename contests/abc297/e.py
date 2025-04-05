import heapq

N, K = map(int, input().split())
A = [int(i) for i in input().split()]

hq = A[::]
heapq.heapify(hq)

done = set()

cnt = 0
while True:
    x = heapq.heappop(hq)
    if x not in done:
        done.add(x)
        for a in A:
            heapq.heappush(hq, x + a)
        cnt += 1

    if cnt == K:
        print(x)
        break
