import sys, heapq
input = sys.stdin.readline

N, Q = map(int, input().split())

event = []
for _ in range(N) :
    s, t, x = map(int, input().split())
    event.append([s - x, t - x, x])

D = [int(input()) for _ in range(Q)]

event.sort()

closed = []
ei = 0

for d in D :
    while ei < N and event[ei][0] <= d :
        heapq.heappush(closed, (event[ei][2], event[ei][1]))
        ei += 1
    while closed and closed[0][1] <= d :
        heapq.heappop(closed)
    
    if closed :
        print(closed[0][0])
    else :
        print(-1)