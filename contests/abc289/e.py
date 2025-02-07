import collections

T = int(input())


def solve(N, M, C, uv):
    graph = [[] for _ in range(N)]
    for u, v in uv:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    queue = collections.deque([(0, N - 1, 0)])
    visited = set()
    while queue:
        cp1, cp2, ccost = queue.popleft()
        for np1 in graph[cp1]:
            for np2 in graph[cp2]:
                if (np1, np2) in visited:
                    continue
                if C[np1] == C[np2]:
                    continue
                if np1 == N - 1 and np2 == 0:
                    return ccost + 1

                visited.add((np1, np2))
                queue.append((np1, np2, ccost + 1))

    return -1


for _ in range(T):
    N, M = map(int, input().split())
    C = [int(i) for i in input().split()]
    uv = [[int(i) for i in input().split()] for _ in range(M)]
    print(solve(N, M, C, uv))
