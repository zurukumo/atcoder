N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
for A, B in AB:
    ret += (A + B) * (B - A + 1) // 2

print(ret)
