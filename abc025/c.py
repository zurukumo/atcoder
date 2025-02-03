b = [[int(i) for i in input().split()] for _ in range(2)]
c = [[int(i) for i in input().split()] for _ in range(3)]

field = [[-1] * 3 for _ in range(3)]


def dfs(n):
    if n == 9:
        x, y = 0, 0
        for i in range(3):
            for j in range(3):
                if i < 2:
                    if field[i][j] == field[i + 1][j]:
                        x += b[i][j]
                    else:
                        y += b[i][j]
                if j < 2:
                    if field[i][j] == field[i][j + 1]:
                        x += c[i][j]
                    else:
                        y += c[i][j]
        return x, y

    mx, my = -float("inf"), -float("inf")
    for i in range(3):
        for j in range(3):
            if field[i][j] >= 0:
                continue
            field[i][j] = n % 2
            x, y = dfs(n + 1)
            if n % 2 == 0:
                if x > mx:
                    mx, my = x, y
            else:
                if y > my:
                    mx, my = x, y
            field[i][j] = -1

    return mx, my


ret = dfs(0)
print(ret[0])
print(ret[1])
