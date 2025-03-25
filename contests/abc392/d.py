N = int(input())
KA = [[int(i) for i in input().split()] for _ in range(N)]

a_dict = [dict() for _ in range(N)]
for i in range(N):
    for j in KA[i][1:]:
        if j not in a_dict[i]:
            a_dict[i][j] = 0
        a_dict[i][j] += 1

ret = -float("inf")
for i in range(N):
    for j in range(i + 1, N):
        s = 0
        for k, v in a_dict[i].items():
            if k in a_dict[j]:
                s += v * a_dict[j][k]
        ret = max(ret, s / (sum(a_dict[i].values()) * sum(a_dict[j].values())))

print(ret)
