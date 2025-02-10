import heapq

N = int(input())
TD = [[int(i) for i in input().split()] for _ in range(N)]


hq1 = []
for t, d in TD:
    heapq.heappush(hq1, (t, t + d))

ret = 0
now = -10
hq2 = []
while True:
    while hq1 and hq1[0][0] <= now:
        t_start, t_end = heapq.heappop(hq1)
        heapq.heappush(hq2, (t_end, t_start))

    if hq2:
        t_end, t_start = heapq.heappop(hq2)
        if t_end < now:
            continue
        ret += 1
        now = max(now + 1, t_start)
    elif hq1:
        now = hq1[0][0]
    else:
        break
print(ret)
