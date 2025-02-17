N, D = map(int, input().split())

if N * D > N * (N - 1) // 2:
    print("No")
else:
    print("Yes")
    for i in range(N):
        for j in range(i + 1, i + 1 + D):
            j %= N
            print(i + 1, j + 1)
