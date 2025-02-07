N, M = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

AB.sort()
ret = 0
for A, B in AB:
    if B <= M:
        ret += A * B
        M -= B
    else:
        ret += A * M
        break

print(ret)
