N, M = map(int, input().split())
xyz = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[[0] * 3 for _ in range(8)] for _ in range(N + 1)]

for i, (x, y, z) in enumerate(xyz) :
    