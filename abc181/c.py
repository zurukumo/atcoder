N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]


def judge():
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                xi, yi = xy[i]
                xj, yj = xy[j]
                xk, yk = xy[k]
                if (xi, yi) == (xj, yj) or (xj, yj) == (xk, yk) or (xk, yk) == (xi, yi):
                    continue
                if (xi - xk) * (yj - yk) - (xj - xk) * (yi - yk) == 0:
                    return "Yes"
    return "No"


print(judge())
