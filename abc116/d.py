from heapq import heappush, heappop

N, K = map(int, input().split())
td = [[int(i) for i in input().split()] for _ in range(N)]

counter = [0] * (N + 1)
h = []
for t, d in td :
    counter[t] += 1
    heappush(h, (d, d, t))

kind = len(set(t for t, d in td))
for _ in range(N - K) :
    while True :
        _, d, t = heappop(h)
        if counter[t] == 1 :
            loss = kind * kind - (kind - 1) * (kind - 1) + d
            if loss <= h[0][0] :
                counter[t] -= 1
                kind -= 1
            else :
                heappush(h, (loss, d, t))
                continue
        else :
            counter[t] -= 1
        
        break
        
print(sum(d for _, d, t in h) + kind * kind)