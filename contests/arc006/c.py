N = int(input())
w = [int(input()) for _ in range(N)]

mountain = []

for i in range(N):
    mk, mv = -1, float("inf")
    for j in range(len(mountain)):
        if mountain[j][-1] >= w[i]:
            if mountain[j][-1] < mv:
                mk = j
                mv = mountain[j][-1]

    if mk == -1:
        mountain.append([w[i]])
    else:
        mountain[mk].append(w[i])

print(len(mountain))
