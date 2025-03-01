N = int(input())


for i in range(N):
    T = ""
    for j in range(N):
        diff = min(i, j, N - 1 - i, N - 1 - j)
        if diff % 2 == 0:
            T += "#"
        else:
            T += "."
    print(T)
