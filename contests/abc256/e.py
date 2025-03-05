import heapq

N = int(input())
X = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]


cost = [0] * N
for i in range(N):
    cost[X[i] - 1] += C[i]

queue = []
for i in range(N):
    heapq.heappush(queue, (cost[i], i))

done = [False] * N
ret = 0
while queue:
    c, cur = heapq.heappop(queue)
    if done[cur]:
        continue

    ret += c
    nex = X[cur] - 1
    cost[nex] -= C[cur]
    done[cur] = True
    heapq.heappush(queue, (cost[nex], nex))

print(ret)
