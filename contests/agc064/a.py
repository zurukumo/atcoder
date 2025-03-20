N = int(input())

ret = []
m = 1
for _ in range(N - 3):
    i = N
    while i >= m:
        ret.append(i)
        if i == m:
            break
        i -= 2
    i += 1
    while i <= N:
        ret.append(i)
        i += 2
    m += 1

ret.extend([N, N - 1, N, N - 1, N, N - 2])

print(*ret)
