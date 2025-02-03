N = int(input())
c = [i for i in input()]

ret = 0
i, j = 0, N - 1
while i < j:
    while i < N and c[i] != "W":
        i += 1
    while 0 <= j and c[j] != "R":
        j -= 1
    if i < j:
        ret += 1
        c[i], c[j] = c[j], c[i]

print(ret)
