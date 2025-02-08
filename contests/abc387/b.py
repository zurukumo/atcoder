X = int(input())

s = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j != X:
            s += i * j

print(s)
