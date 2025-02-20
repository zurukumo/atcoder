import collections

N = int(input())
A = [[int(i) for i in input().split()] for _ in range(2 * N - 1)]

bits = list(range(1 << N))
bits.sort(key=lambda x: bin(x).count("1"))

ret = -float("inf")
queue = collections.deque([(0, 0)])
while queue:
    bit, fun = queue.popleft()
    if bit == (1 << (2 * N)) - 1:
        ret = max(ret, fun)
        continue

    for i in range(2 * N):
        if bit & (1 << i) == 0:
            bit |= 1 << i
            break

    for j in range(i + 1, 2 * N):
        if bit & (1 << j) == 0:
            queue.append((bit | 1 << j, fun ^ A[i][j - i - 1]))

print(ret)
