N, D = map(int, input().split())
T = [int(i) for i in input().split()]


for i in range(1, N):
    if T[i] - T[i - 1] <= D:
        print(T[i])
        break
else:
    print(-1)
