H = int(input())

s = 0
i = 0
while s <= H:
    s += 2**i
    i += 1
print(i)
