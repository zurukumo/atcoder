import collections

N = int(input())
C = [0] + [int(i) for i in input().split()]
A = [0] + [int(i) for i in input().split()]

beans_idx = [0]
for i, a in enumerate(A):
    if a == 1:
        beans_idx.append(i)

graph = [[] for _ in range(N)]
for i, c in enumerate(C):
    u = max(0, i - c)
    v = i
    while u < v:
        graph[u].append(v)
        u += 1

ret = 0
for i in range(len(beans_idx) - 1):
    u = beans_idx[i]
    v = beans_idx[i + 1]
    visited = set()
    stack = collections.deque([(0, u)])
    visited.add(u)
    while stack:
        co, cur = stack.popleft()
        for nex in graph[cur]:
            if nex not in visited:
                visited.add(nex)
                stack.append((co + 1, nex))
            if nex == v:
                # print(u, "から", v, "は", co + 1)
                ret += co + 1
                break
        else:
            continue
        break


print(ret)
