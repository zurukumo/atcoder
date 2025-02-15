N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

ret = 0
parity = 0
for a, b in AB:
    ret += max(a, b)
    if a > b:
        parity ^= 1

if parity == 1:
    ret -= min(abs(b - a) for a, b in AB)

print(ret)
