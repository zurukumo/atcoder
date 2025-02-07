N, M = map(int, input().split())
ab = [[int(i) for i in input().split()] for _ in range(M)]

ret = [0] * N
for a, b in ab:
    ret[a - 1] += 1
    ret[b - 1] += 1

print("\n".join(map(str, ret)))
