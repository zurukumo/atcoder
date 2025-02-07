HA, WA = map(int, input().split())
A = [input() for _ in range(HA)]
HB, WB = map(int, input().split())
B = [input() for _ in range(HB)]
HX, WX = map(int, input().split())
X = [input() for _ in range(HX)]


def convet_to_dots(arr):
    dots = set()
    for h in range(len(arr)):
        for w in range(len(arr[0])):
            if arr[h][w] == "#":
                dots.add((h, w))
    return dots


def merge_dots(a_dots, b_dots, dy, dx):
    c_dots = a_dots.copy()
    for y, x in b_dots:
        c_dots.add((y + dy, x + dx))
    return c_dots


def trim(dots):
    min_y = float("inf")
    min_x = float("inf")
    for y, x in dots:
        min_y = min(min_y, y)
        min_x = min(min_x, x)

    return set([(y - min_y, x - min_x) for y, x in dots])


a_dots = convet_to_dots(A)
b_dots = convet_to_dots(B)
x_dots = convet_to_dots(X)

for dy in range(-20, 21):
    for dx in range(-20, 21):
        c_dots = merge_dots(a_dots, b_dots, dy, dx)
        if trim(c_dots) == trim(x_dots):
            print("Yes")
            exit()

print("No")
