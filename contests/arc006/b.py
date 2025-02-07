N, L = map(int, input().split())
x = [list(input()) for _ in range(L)]
y = list(input())

cx = y.index("o")
while x:
    if 0 <= cx - 1 <= 2 * (N - 1) and x[-1][cx - 1] == "-":
        cx -= 2
    elif 0 <= cx + 1 <= 2 * (N - 1) and x[-1][cx + 1] == "-":
        cx += 2

    x.pop()

print(cx // 2 + 1)
