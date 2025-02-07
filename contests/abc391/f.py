import heapq

N, K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)


def calc(a, b, c):
    return a * b + b * c + c * a


visited = set()

queue = [(-calc(A[0], B[0], C[0]), 0, 0, 0)]
visited.add((0, 0, 0))
ans = []
while len(ans) < K:
    v, i, j, k = heapq.heappop(queue)
    ans.append(-v)
    if i + 1 < N and (i + 1, j, k) not in visited:
        heapq.heappush(queue, (-calc(A[i + 1], B[j], C[k]), i + 1, j, k))
        visited.add((i + 1, j, k))
    if j + 1 < N and (i, j + 1, k) not in visited:
        heapq.heappush(queue, (-calc(A[i], B[j + 1], C[k]), i, j + 1, k))
        visited.add((i, j + 1, k))
    if k + 1 < N and (i, j, k + 1) not in visited:
        heapq.heappush(queue, (-calc(A[i], B[j], C[k + 1]), i, j, k + 1))
        visited.add((i, j, k + 1))

print(ans[K - 1])
