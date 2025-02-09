N, M = map(int, input().split())
AB = [input().split() for _ in range(M)]

men = [0] * N
for a, b in AB:
    a = int(a) - 1
    if b == "M" and men[a] == 0:
        print("Yes")
        men[a] += 1
    else:
        print("No")
