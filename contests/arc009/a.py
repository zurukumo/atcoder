N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for a, b in ab:
    ret += a * b

print(int(ret * 1.05))
