import heapq

K, N, M = map(int, input().split())
A = [int(i) for i in input().split()]

B = []
plus = []
minus = []

for i, a in enumerate(A):
    b = round(a * M / N)
    cur_diff = abs(b * N - a * M)
    plus_diff = abs((b + 1) * N - a * M)
    minus_diff = abs((b - 1) * N - a * M)
    B.append(b)
    heapq.heappush(plus, (plus_diff, i))
    heapq.heappush(minus, (minus_diff, i))

s = sum(B)
while s < M:
    _, i = heapq.heappop(plus)
    B[i] += 1
    s += 1
    heapq.heappush(plus, (abs((B[i] + 1) * N - A[i] * M), i))
while s > M:
    _, i = heapq.heappop(minus)
    B[i] -= 1
    s -= 1
    heapq.heappush(minus, (abs((B[i] - 1) * N - A[i] * M), i))
print(*B)
