b = [list(input()) for _ in range(19)]


def check():
    win = {"o": 0, "x": 0, ".": 0}
    for i in range(19):
        for j in range(19):
            for ud in [-1, 0, 1]:
                for lr in [-1, 0, 1]:
                    if ud == lr == 0:
                        continue
                    if 0 <= i + ud * 4 < 19 and 0 <= j + lr * 4 < 19:
                        s = set(b[i + ud * k][j + lr * k] for k in range(5))
                        if len(s) == 1:
                            win[s.pop()] += 1

    return (win["o"], win["x"])


def solve():
    o, x = 0, 0
    for i in range(19):
        for j in range(19):
            if b[i][j] == "o":
                o += 1
            if b[i][j] == "x":
                x += 1

    wo, wx = check()

    # ありえない石の数
    if o != x and o != x + 1:
        return "NO"

    if wx == wo == 0:
        return "YES"

    if o == x:
        if wx == 0:
            return "NO"
        last = "x"
    if o == x + 1:
        if wo == 0:
            return "NO"
        last = "o"

    for i in range(19):
        for j in range(19):
            if b[i][j] == last:
                b[i][j] = "."
                if check() == (0, 0):
                    return "YES"
                b[i][j] = last

    return "NO"


print(solve())
