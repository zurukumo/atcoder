N = int(input())


print("".join(str(1 - i % 2) for i in range(2 * N + 1)))
