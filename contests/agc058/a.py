N = int(input())
P = [int(i) for i in input().split()]


ret = []
for i in range(2 * N - 1):
    if i % 2 == 0:
        if P[i] > P[i + 1]:
            if i + 2 < 2 * N and P[i + 2] > P[i]:
                ret.append(i + 2)
                P[i + 1], P[i + 2] = P[i + 2], P[i + 1]
            else:
                ret.append(i + 1)
                P[i], P[i + 1] = P[i + 1], P[i]
    else:
        if P[i] < P[i + 1]:
            if i + 2 < 2 * N and P[i + 2] < P[i]:
                ret.append(i + 2)
                P[i + 1], P[i + 2] = P[i + 2], P[i + 1]
            else:
                ret.append(i + 1)
                P[i], P[i + 1] = P[i + 1], P[i]

print(len(ret))
print(*ret)
