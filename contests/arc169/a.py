N = int(input())
A = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]

graph = [[] for _ in range(N)]
for i, p in enumerate(P):
    graph[p - 1].append(i + 1)

cost = [A[0]]
queue = [(0, 0)]
while queue:
    cur, cc = queue.pop()
    for nex in graph[cur]:
        if len(cost) <= cc:
            cost.append(A[nex])
        else:
            cost[cc] += A[nex]
        queue.append((nex, cc + 1))


while cost and cost[-1] == 0:
    cost.pop()

if not cost:
    print("0")
elif cost[-1] > 0:
    print("+")
elif cost[-1] < 0:
    print("-")
