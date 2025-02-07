N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

s = 0
for A, B in AB[::-1]:
    x = (A + s + B - 1) // B
    s += x * B - (A + s)

print(s)
