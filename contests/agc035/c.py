N = int(input())

M = N
while M % 2 == 0:
    M //= 2

if M == 1 or N < 3:
    print("No")
else:
    print("Yes")
    print(3, 1)
    print(1, 2)
    print(2, 3 + N)
    print(3 + N, 1 + N)
    print(1 + N, 2 + N)

    for i in range(4, N, 2):
        print(1, i + 1)
        print(i + 1, i)
        print(1, N + i)
        print(N + i, N + i + 1)

    if N % 2 == 0:
        i = 1
        while True:
            if N >> i & 1:
                break
            i += 1
        print((1 << i) + 1, N)
        print(2 * N - (1 << i), 2 * N)
