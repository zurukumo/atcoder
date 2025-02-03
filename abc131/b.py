N, L = map(int, input().split())

s = 0
for i in range(1, N + 1):
    s += L + i - 1

zettaici = float('inf')
jissai = 0
for i in range(1, N + 1):
    x = L + i - 1
    if abs(x) < zettaici:
        zettaici = abs(x)
        jissai = x

print(s - jissai)
