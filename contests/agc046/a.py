X = int(input())

for i in range(1, 10**10):
    if (i * X) % 360 == 0:
        print(i)
        break
