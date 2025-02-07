from sortedcontainers import SortedList

N, M = map(int, input().split())
A = [int(i) for i in input().split()]
UV = [[int(i) for i in input().split()] for _ in range(M)]


vec = [set() for _ in range(N)]
for u, v in UV:
    vec[u - 1].add(v - 1)
    vec[v - 1].add(u - 1)


around_cost = SortedList()
current_v = [0] * N
for i in range(N):
    s = 0
    for j in vec[i]:
        s += A[j]
    around_cost.add((s, i))
    current_v[i] = s


ret = -float("inf")
while around_cost:
    s, i = around_cost.pop(0)
    ret = max(ret, s)
    for j in vec[i]:
        around_cost.remove((current_v[j], j))
        current_v[j] -= A[i]
        around_cost.add((current_v[j], j))
        vec[j].remove(i)

print(ret)
