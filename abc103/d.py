from heapq import heappush, heappop

N, M = map(int, input().split())

ab = [[int(i) for i in input().split()] for _ in range(M)]

ab.sort(key=lambda x: x[1])
ab.sort()

ret = 1
end = float("inf")
for a, b in ab:
    if a >= end:
        ret += 1
        end = b
    else:
        end = min(end, b)

print(ret)
