N = int(input())

for i in range(1, 10**9):
    if i * (i + 1) // 2 >= N:
        print(i)
        break
